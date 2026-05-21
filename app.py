import sys


def get_version():
    try:
        with open("./version.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("version.txt file doesn't exist", file=sys.stderr)
        sys.exit(1)


print(get_version())
