# DTop

![Platform](https://img.shields.io/badge/platform-Linux-blue)
![License](https://img.shields.io/badge/license-MIT-green)

dtop is a terminal-based process manager built with Python, [Textual](https://github.com/Textualize/textual), and psutil. Search processes by name, kill them with a keystroke, and toggle between light and dark mode. All from your terminal. Inspired by [htop](https://github.com/htop-dev/htop).

## Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3 |
| TUI Framework | Textual |
| System Info | psutil |
| Platform | Linux |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dincertekin/dtop.git
   cd dtop/
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python dtop.py
```

If you run into dependency issues, make sure pip is up to date:
```bash
pip install --upgrade pip
```

## Controls

| Key | Action |
|---|---|
| `Ctrl+Q` | Quit the application |
| `D` | Toggle dark mode |
| `Ctrl+S` | Search processes by name |
| `K` | Kill selected process |
| Arrow keys | Navigate process list |

## Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT License](./LICENSE)
