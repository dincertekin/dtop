# dtop

[![license: MIT](https://img.shields.io/badge/license-MIT-111827)](LICENSE)
![Python 3](https://img.shields.io/badge/python-3-111827?logo=python)
![Built with Textual](https://img.shields.io/badge/built%20with-Textual-111827)

**A friendlier `htop`.** See what's running, sort by CPU or memory, search by
name and kill a process with one key, in a modern terminal UI that also works
with your mouse.

- **Live:** refreshes every 2 seconds, with heavy processes colored so they stand out.
- **Search:** filter the list by process name as you type.
- **Safe kills:** `k` asks for confirmation before ending anything.
- **Light or dark:** switch with `d`.

## Install

```bash
git clone https://github.com/dincertekin/dtop.git
cd dtop
pip install -r requirements.txt
python main.py
```

Developed on Linux. It's built on [psutil](https://github.com/giampaolo/psutil)
and [Textual](https://github.com/Textualize/textual), which also run on macOS
and Windows.

## Keys

| Key | Action |
|---|---|
| `↑` `↓` | Move through the list |
| `Ctrl+S` | Search by name |
| `Esc` | Clear the search |
| `c` / `m` | Sort by CPU / memory |
| `k` | Kill the selected process (asks first) |
| `d` | Toggle dark mode |
| `Ctrl+Q` | Quit |

Killing processes you don't own needs `sudo python main.py`.

## Contributing

Issues and pull requests are welcome.

Inspired by [htop](https://github.com/htop-dev/htop).

## License

[MIT](LICENSE)
