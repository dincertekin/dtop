import psutil
from rich.text import Text
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, DataTable

ROWS = [
    ("pid", "name", "username"),
]

for proc in psutil.process_iter(['pid', 'name', 'username']):
#    print(proc.info)
    ROWS.append([proc.info.get("pid"), proc.info.get("name"), proc.info.get("username")])

class DTopApp(App):
    """A Textual app to see and manage processes."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("k", "kill_process", "Kill Selected Process"),
        ("ctrl+q", "quit", "Quit")
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield DataTable(cursor_type="row")
        yield Footer()

    def on_mount(self) -> None:
        """ When the app mounted: """
        table = self.query_one(DataTable)
        table.styles.min_width = "100%" # TODO: didnt work, gonna fix
        table.add_columns(*ROWS[0])
        for row in ROWS[1:]:
            styled_row = [
                Text(str(cell), style="italic #03AC13", justify="right") for cell in row
            ]
            table.add_row(*styled_row)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = DTopApp()
    app.run()