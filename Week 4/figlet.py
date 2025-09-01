import sys
import pyfiglet

def main():
    if len(sys.argv) == 1:
        font = pyfiglet.Figlet()
    elif len(sys.argv) == 3 and sys.argv[1] in ('-f', '--font'):
        font_name = sys.argv[2]
        try:
            font = pyfiglet.Figlet(font=font_name)
        except pyfiglet.FontNotFound:
            print(f"Error: Font '{font_name}' not found.")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)

    text = input("Input: ")
    render = font.renderText(text)
    print(render)



main()
