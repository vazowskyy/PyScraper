import sys
from functions.get_html import get_html

def main():

    if len(sys.argv) < 2:
        print("no website provided! Here's an example: uv run example.py -v")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("too many arguments provided! Here's an example: uv run example.py -v")
        sys.exit(1)
    else:
        BASE_URL = sys.argv[1]
        print(f"starting crawl of: {BASE_URL}")

    content = get_html(BASE_URL)
    print(content)


if __name__ == "__main__":
    main()
