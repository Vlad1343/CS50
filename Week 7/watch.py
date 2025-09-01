import re
import sys

def main():
    html_input = input("HTML: ")
    parsed_url = parse(html_input)
    print(parsed_url)

def parse(s):
    pattern = r"<iframe.*?src=\"(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)\".*?>"
    match = re.search(pattern, s)

    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
