# dtop

**dtop** is a modern TUI process manager built with [Textual](https://github.com/Textualize/textual). It allows you to view and manage system processes. You can toggle dark mode, search for processes by name, and kill processes directly from the terminal.

## Features

- Toggle between light and dark mode
- Search processes (`Ctrl+S`)
- Kill selected processes (`K`)
- Dynamic, full-width rainbow-styled task list
- Built with Python, using Textual and psutil

## Installation

You can install dtop using pip.

### Installing with pip

```bash
git clone https://github.com/dincertekin/dtop.git
cd dtop/
pip install -r requirements.txt
python dtop.py
```

## Controls

| Key        | Action                   |
| ---------- | ------------------------ |
| `Ctrl+Q`   | Quit the application     |
| `D`        | Toggle dark mode         |
| `Ctrl+S`   | Search processes by name |
| `K`        | Kill selected process    |
| Arrow keys | Navigate process list    |

## Contributions

Contributions are very welcome! We can improve this tool together! 😊

## License

This project is licensed under the [MIT License](LICENSE).

## Thanks

Inspired by classic tools like [htop](https://github.com/htop-dev/htop).
