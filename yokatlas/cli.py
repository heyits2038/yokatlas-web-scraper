"""
    Author: @heyits2038
    GitHub: https://github.com/heyits2038
"""
import sys
import pyfiglet
import webbrowser
import questionary

from yokatlas.utils import logger


CHOICES = {
    "fetch_programs": "📖 Fetch Programs",
    "github": "🐙 GitHub",
    "issues": "🐛 Issues",
    "exit": "❌ Exit"
}


def open_web_browser(url: str) -> None:
    """
    Opens a web browser to the given URL.
    """
    webbrowser.open(url)


def print_welcome() -> None:
    """
    Prints a welcome message.
    """
    print(pyfiglet.figlet_format("YokAtlas", font="slant"))
    print(pyfiglet.figlet_format("Web Scraper", font="slant"))
    print("⚠️  This program is for educational purposes only.\n")


def main() -> None:
    """"
    Main function to run the CLI.
    """
    print_welcome()

    choice = questionary.select(
        "What would you like to do?",
        choices=list(CHOICES.values())
    ).ask()

    try:
        if choice == CHOICES["fetch_programs"]:
            logger.warning("Not implemented yet.")
        elif choice == CHOICES["github"]:
            open_web_browser(
                "https://github.com/heyits2038/yokatlas-web-scraper")
        elif choice == CHOICES["issues"]:
            open_web_browser(
                "https://github.com/heyits2038/yokatlas-web-scraper/issues")
        elif choice == CHOICES["exit"]:
            sys.exit(0)
        else:
            logger.error("Invalid selection.")
    except NotImplementedError as e:
        logger.error(f"Error: {e}")
    except (KeyboardInterrupt, SystemExit):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
