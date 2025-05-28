import sys

from rich.console import Console
from rich.markdown import Markdown

console = Console()


def main():
    if len(sys.argv) > 1:
        # Read from file
        filename = sys.argv[1]
        try:
            with open(filename) as f:
                content = f.read()
        except Exception as e:
            console.print(f"[red]Error reading file:[/red] {e}")
            sys.exit(1)
    elif not sys.stdin.isatty():
        # Read from piped stdin
        content = sys.stdin.read()
    else:
        console.print("[yellow]Usage:[/yellow] par-md <filename> or cat file.md | par-md")
        sys.exit(1)

    console.print(Markdown(content))


if __name__ == "__main__":
    main()
