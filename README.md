# PAR MD

## Description

PAR MD displays markdown files in the terminal using rich formatting. It supports both console output and an interactive TUI mode with navigation features.

## Screenshot
![Screenshot of PAR MD](https://raw.githubusercontent.com/paulrobello/par_md/main/Screenshot.png)


## Installation

Astral uv is recommended for installing PAR MD.

### Install uv

* MacOS 
```bash
brew install uv
```

* Windows Powershell
```powershell 
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

* Windows Scoop
```cmd
scoop bucket add main
scoop install main/uv
```

* Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### Install PAR MD
```bash
uv tool install "git+https://github.com/paulrobello/par_md"
```


## Usage

PAR MD supports two display modes: console mode (default) and interactive TUI mode.

### Console Mode (Default)

Specify a markdown file to display it in the terminal with rich formatting:
```bash
par-md <file.md>
```

If you want to pipe a markdown file into PAR MD, you can use:
```bash
cat <file.md> | par-md 
```

### Interactive TUI Mode

Launch the interactive Text User Interface mode for enhanced navigation:
```bash
par-md --tui <file.md>
```

You can also pipe content to TUI mode:
```bash
cat <file.md> | par-md --tui
```

#### TUI Features

- **Header**: Shows filename and application title
- **Table of Contents**: Collapsible sidebar for easy navigation
- **Footer**: Displays available key bindings
- **Interactive Navigation**: Vim-like key bindings for scrolling

#### Key Bindings

- `q` or `Ctrl+C`: Quit application
- `h`: Toggle table of contents visibility
- `j`: Scroll down
- `k`: Scroll up
- `g`: Go to top of document
- `G`: Go to bottom of document
- `^p`: Open command palette

### Help

View all available options:
```bash
par-md --help
```
