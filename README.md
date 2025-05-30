# PAR MD

## Description

PAR MD displays markdown files in the terminal using rich formatting.

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

Specify a markdown file to display it in the terminal:
```bash
par-md <file.md>
```

If you want to pipe a markdown file into PAR MD, you can use:
```bash
cat <file.md> | par-md 
```
