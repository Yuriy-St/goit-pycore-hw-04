import sys
from pathlib import Path
from colorama import Fore


def colorize_path(root: Path, level=0):
    folders = sorted([d for d in root.iterdir() if d.is_dir()])
    files = sorted([f for f in root.iterdir() if f.is_file()])

    if level == 0:
        print(f"{Fore.RED}{root.name}/{Fore.RESET}")
        level += 1

    indent = "  " * level
    for item in folders + files:
        if item.is_dir():
            print(f"{indent}📂 {Fore.RED}{item.name}/{Fore.RESET}")
            colorize_path(item, level + 1)
        else:
            print(f"{indent}📄 {Fore.CYAN}{item.name}{Fore.RESET}")


def main():
    if len(sys.argv) < 2:
        print(f"Incorrect number of arguments")
        sys.exit(1)

    try:
        root = Path(sys.argv[1])
        colorize_path(root)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
