import psutil
from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, DataTable, Input
from textual import events

class DTopApp(App):
    """A Textual app to see and manage processes."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("k", "kill_process", "Kill Selected Process"),
        ("ctrl+q", "quit", "Quit"),
        ("ctrl+s", "start_search", "Search Process"),
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

    RAINBOW_COLORS = ["#FF5555", "#F1FA8C", "#50FA7B", "#8BE9FD", "#BD93F9", "#FF79C6"]

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
        self.refresh_processes()
        self.table.focus()

    def refresh_processes(self, filter_str: str = "") -> None:
        self.table.clear(columns=True)
        self.table.add_columns("PID", "Name", "Username")

        for idx, proc in enumerate(psutil.process_iter(['pid', 'name', 'username'])):
            try:
                pid = proc.info.get("pid")
                name = proc.info.get("name", "N/A")
                username = proc.info.get("username", "N/A")

                if filter_str.lower() not in name.lower():
                    continue

                color = self.RAINBOW_COLORS[idx % len(self.RAINBOW_COLORS)]
                styled_row = [
                    Text(str(pid), style=f"bold {color}", justify="right"),
                    Text(name, style=f"bold {color}", justify="right"),
                    Text(username, style=f"bold {color}", justify="right"),
                ]
                self.table.add_row(*styled_row)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_kill_process(self) -> None:
        if self.table.cursor_row is None:
            return
        row = self.table.get_row_at(self.table.cursor_row)
        pid = int(row[0].plain)
        try:
            psutil.Process(pid).terminate()
            self.refresh_processes()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    def action_start_search(self) -> None:
        self.search_input.display = True
        self.search_input.focus()

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        query = message.value.strip()
        self.search_input.display = False
        self.refresh_processes(filter_str=query)
        self.table.focus()

if __name__ == "__main__":
    app = DTopApp()
    app.run()
