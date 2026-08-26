import psutil
from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.screen import ModalScreen
from textual.widgets import Footer, Header, DataTable, Input, Label, Button
from textual.containers import Vertical, Horizontal


class ConfirmKillScreen(ModalScreen):
    """Modal that asks the user to confirm killing a process."""

    CSS = """
    ConfirmKillScreen {
        align: center middle;
    }

    #dialog {
        width: 50;
        height: auto;
        border: thick $background 80%;
        background: $surface;
        padding: 1 2;
    }

    #buttons {
        margin-top: 1;
        align: center middle;
    }

    Button {
        margin: 0 1;
    }
    """

    def __init__(self, pid: int, name: str) -> None:
        super().__init__()
        self.pid = pid
        self.name = name

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Label(f"Kill process {self.name} (PID {self.pid})?")
            with Horizontal(id="buttons"):
                yield Button("Kill", id="confirm", variant="error")
                yield Button("Cancel", id="cancel", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "confirm")


class DTopApp(App):
    """A Textual app to see and manage processes."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("k", "kill_process", "Kill Selected Process"),
        ("ctrl+q", "quit", "Quit"),
        ("ctrl+s", "start_search", "Search Process"),
        ("escape", "clear_search", "Clear Search"),
        ("c", "sort_cpu", "Sort by CPU"),
        ("m", "sort_mem", "Sort by Memory"),
    ]

    CSS = """
    Screen > Container {
        layout: vertical;
    }

    DataTable {
        height: 1fr;
        width: 100%;
    }

    Input#search_input {
        dock: top;
        width: 100%;
    }
    """

    REFRESH_INTERVAL = 2.0  # seconds between automatic refreshes

    def __init__(self) -> None:
        super().__init__()
        self.filter_str = ""
        self.sort_key = "cpu_percent"  # default sort column

    def compose(self) -> ComposeResult:
        yield Header()
        with Container():
            self.table = DataTable(cursor_type="row")
            yield self.table
        self.search_input = Input(placeholder="Search by process name...", id="search_input")
        self.search_input.display = False
        yield self.search_input
        yield Footer()

    def on_mount(self) -> None:
        self.table.add_columns("PID", "Name", "Username", "CPU%", "MEM%")
        # Prime cpu_percent so the first real reading isn't always 0.0
        for proc in psutil.process_iter():
            try:
                proc.cpu_percent(interval=None)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        self.refresh_processes()
        self.table.focus()
        self.set_interval(self.REFRESH_INTERVAL, self.refresh_processes)

    def refresh_processes(self) -> None:
        # Remember the selected PID so the cursor doesn't jump around on refresh.
        selected_pid = None
        if self.table.row_count and self.table.cursor_row is not None:
            try:
                selected_pid = int(self.table.get_row_at(self.table.cursor_row)[0].plain)
            except Exception:
                selected_pid = None

        self.table.clear()

        rows = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
            try:
                pid = proc.info.get("pid")
                name = proc.info.get("name") or "N/A"
                username = proc.info.get("username") or "N/A"
                cpu = proc.info.get("cpu_percent") or 0.0
                mem = proc.info.get("memory_percent") or 0.0

                if self.filter_str and self.filter_str.lower() not in name.lower():
                    continue

                rows.append((pid, name, username, cpu, mem))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        rows.sort(key=lambda r: r[3] if self.sort_key == "cpu_percent" else r[4], reverse=True)

        new_cursor_row = 0
        for idx, (pid, name, username, cpu, mem) in enumerate(rows):
            color = self._color_for_usage(max(cpu, mem))
            styled_row = [
                Text(str(pid), style=color),
                Text(name, style=color),
                Text(username, style=color),
                Text(f"{cpu:.1f}", style=color, justify="right"),
                Text(f"{mem:.1f}", style=color, justify="right"),
            ]
            self.table.add_row(*styled_row)
            if selected_pid is not None and pid == selected_pid:
                new_cursor_row = idx

        if self.table.row_count:
            self.table.move_cursor(row=new_cursor_row)

    @staticmethod
    def _color_for_usage(value: float) -> str:
        """Color-code by resource usage instead of arbitrary rainbow."""
        if value >= 50:
            return "bold red"
        if value >= 20:
            return "bold yellow"
        return "white"

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_sort_cpu(self) -> None:
        self.sort_key = "cpu_percent"
        self.refresh_processes()

    def action_sort_mem(self) -> None:
        self.sort_key = "memory_percent"
        self.refresh_processes()

    def action_kill_process(self) -> None:
        if self.table.row_count == 0 or self.table.cursor_row is None:
            return
        row = self.table.get_row_at(self.table.cursor_row)
        pid = int(row[0].plain)
        name = row[1].plain

        def handle_confirmation(confirmed: bool | None) -> None:
            if not confirmed:
                return
            try:
                p = psutil.Process(pid)
                p.terminate()
                try:
                    p.wait(timeout=2)
                except psutil.TimeoutExpired:
                    # Process ignored SIGTERM, escalate to SIGKILL.
                    p.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            self.refresh_processes()

        self.push_screen(ConfirmKillScreen(pid, name), handle_confirmation)

    def action_start_search(self) -> None:
        self.search_input.display = True
        self.search_input.focus()

    def action_clear_search(self) -> None:
        if self.filter_str:
            self.filter_str = ""
            self.refresh_processes()
        self.search_input.display = False
        self.table.focus()

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        self.filter_str = message.value.strip()
        self.search_input.display = False
        self.refresh_processes()
        self.table.focus()


if __name__ == "__main__":
    app = DTopApp()
    app.run()
