"""
    Author: @heyits2038
    GitHub: https://github.com/heyits2038
"""
import sys
import questionary
import pyfiglet


CHOICES = {
    "bachelor": "📘 Bachelor's Degree Programs",
    "associate": "📗 Associate Degree Programs",
    "exit": "❌ Exit"
}


def main() -> None:
    """"
    Displays a welcome message and prompts the user to select a degree program to fetch.
    """
    print(pyfiglet.figlet_format("YokAtlas", font="slant"))
    print(pyfiglet.figlet_format("Web Scraper", font="slant"))

    print("⚠️  This program is for educational purposes only.\n")

    choice = questionary.select(
        "🎓 Which type of degree program would you like to fetch?",
        choices=list(CHOICES.values())
    ).ask()

    try:
        if choice == CHOICES["bachelor"]:
            pass
        elif choice == CHOICES["associate"]:
            pass
        elif choice == CHOICES["exit"]:
            sys.exit(0)
        else:
            print("\nInvalid selection.\n")
    except NotImplementedError as e:
        print(f"\n[ERROR]: {e}\n")
    except (KeyboardInterrupt, SystemExit):
        print("\nGoodbye!\n")


if __name__ == "__main__":
    main()
