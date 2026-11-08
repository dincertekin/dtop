# dtop

<p>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/dincertekin/dincertekin/main/assets/badges/python-dark.svg"><img src="https://raw.githubusercontent.com/dincertekin/dincertekin/main/assets/badges/python-light.svg" alt="Python 3" height="28"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/dincertekin/dincertekin/main/assets/badges/textual-dark.svg"><img src="https://raw.githubusercontent.com/dincertekin/dincertekin/main/assets/badges/textual-light.svg" alt="Textual" height="28"></picture>
  <a href="LICENSE"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/dincertekin/dincertekin/main/assets/badges/mit-dark.svg"><img src="https://raw.githubusercontent.com/dincertekin/dincertekin/main/assets/badges/mit-light.svg" alt="MIT license" height="28"></picture></a>
</p>

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
