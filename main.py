import argparse
import sys
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, MarkdownViewer



class MarkdownTUIApp(App[None]):
    """A Textual app to display markdown files interactively."""

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("ctrl+c", "quit", "Quit"),
        Binding("h", "toggle_table_of_contents", "Toggle TOC"),
        Binding("j", "scroll_down", "Scroll Down"),
        Binding("k", "scroll_up", "Scroll Up"),
        Binding("g", "scroll_home", "Top"),
        Binding("G", "scroll_end", "Bottom"),
    ]

    def __init__(self, content: str, title: str = "PAR MD") -> None:
        super().__init__()
        self.markdown_content = content
        self.title = title
        self.sub_title = "Interactive Markdown Viewer"

    def compose(self) -> ComposeResult:
        """Create the TUI layout with Header, MarkdownViewer, and Footer."""
        yield Header()
        yield MarkdownViewer(
            markdown=self.markdown_content,
            show_table_of_contents=True,
            id="markdown_viewer"
        )
        yield Footer()

    async def action_quit(self) -> None:
        """Exit the application."""
        self.exit()

    async def action_toggle_table_of_contents(self) -> None:
        """Toggle the table of contents visibility."""
        markdown_viewer = self.query_one("#markdown_viewer", MarkdownViewer)
        markdown_viewer.show_table_of_contents = not markdown_viewer.show_table_of_contents

    async def action_scroll_down(self) -> None:
        """Scroll the markdown viewer down."""
        markdown_viewer = self.query_one("#markdown_viewer", MarkdownViewer)
        markdown_viewer.scroll_down()

    async def action_scroll_up(self) -> None:
        """Scroll the markdown viewer up."""
        markdown_viewer = self.query_one("#markdown_viewer", MarkdownViewer)
        markdown_viewer.scroll_up()

    async def action_scroll_home(self) -> None:
        """Scroll to the top of the document."""
        markdown_viewer = self.query_one("#markdown_viewer", MarkdownViewer)
        markdown_viewer.scroll_home()

    async def action_scroll_end(self) -> None:
        """Scroll to the bottom of the document."""
        markdown_viewer = self.query_one("#markdown_viewer", MarkdownViewer)
        markdown_viewer.scroll_end()


def read_markdown_content(filename: str | None = None) -> tuple[str, str]:
    """Read markdown content from file or stdin.

    Args:
        filename: Path to markdown file, None for stdin

    Returns:
        Tuple of (content, display_title)

    Raises:
        SystemExit: If file cannot be read
    """
    console = Console()

    if filename:
        try:
            with open(filename, encoding="utf-8") as f:
                content = f.read()
            return content, f"PAR MD - {Path(filename).name}"
        except Exception as e:
            console.print(f"[red]Error reading file:[/red] {e}")
            sys.exit(1)
    elif not sys.stdin.isatty():
        content = sys.stdin.read()
        return content, "PAR MD - stdin"
    else:
        console.print("[yellow]Usage:[/yellow] par-md [--tui] <filename> or cat file.md | par-md [--tui]")
        sys.exit(1)


def show_markdown_console(content: str) -> None:
    """Display markdown content using rich console."""
    console = Console()
    console.print(Markdown(content))


def show_markdown_tui(content: str, title: str) -> None:
    """Display markdown content using Textual TUI."""
    app = MarkdownTUIApp(content, title)
    app.run()


def main() -> None:
    """Main entry point for PAR MD."""
    parser = argparse.ArgumentParser(
        description="Display markdown files in the terminal with rich formatting",
        prog="par-md"
    )
    parser.add_argument(
        "filename",
        nargs="?",
        help="Markdown file to display (omit to read from stdin)"
    )
    parser.add_argument(
        "--tui",
        action="store_true",
        help="Launch interactive TUI mode"
    )

    args = parser.parse_args()

    # Read markdown content
    content, title = read_markdown_content(args.filename)

    # Display content based on mode
    if args.tui:
        show_markdown_tui(content, title)
    else:
        show_markdown_console(content)


if __name__ == "__main__":
    main()
