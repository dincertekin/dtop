# dtop
Modern TUI process manager built with Python and Textual.

## Description
dtop is a terminal-based process manager built with Python, [Textual](https://github.com/Textualize/textual), and psutil. It lets you view and manage system processes directly from your terminal with a clean, dynamic interface. You can search for processes by name, kill them with a keystroke, and toggle between light and dark mode.

## Getting Started

### Dependencies
* Linux
* Python 3.x
* pip

### Installing

* Clone the repository:
```bash
git clone https://github.com/dincertekin/dtop.git
cd dtop/
```

* Install dependencies:
```bash
pip install -r requirements.txt
```

### Executing program

* Run the tool:
```bash
python dtop.py
```

## Controls
| Key | Action |
|---|---|
| `Ctrl+Q` | Quit the application |
| `D` | Toggle dark mode |
| `Ctrl+S` | Search processes by name |
| `K` | Kill selected process |
| Arrow keys | Navigate process list |

## Help
If you run into dependency issues, make sure you are using Python 3 and that pip is up to date.

```bash
pip install --upgrade pip
```

## Contributing
Contributions are welcome! To get started:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please open an issue first for major changes to discuss what you'd like to change.

## License
This project is licensed under the [MIT](LICENSE) License - see the LICENSE.md file for details

## Acknowledgments
* Inspired by [htop](https://github.com/htop-dev/htop)
* [Textual](https://github.com/Textualize/textual)
