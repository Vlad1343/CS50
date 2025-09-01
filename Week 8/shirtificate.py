from fpdf import FPDF

def main():
    name = input("Name: ")

    pdf = FPDF(format="A4", unit="mm", orientation="P")
    pdf.set_auto_page_break(False)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(0, 0, 0)
    page_width = pdf.w - 2 * pdf.l_margin
    pdf.cell(page_width, 20, "CS50 Shirtificate", ln=True, align="C")

    img_width = 100
    x = (pdf.w - img_width) / 2
    y = pdf.get_y() + 10
    pdf.image("shirtificate.png", x=x, y=y, w=img_width)

    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)

    text_y = y + img_width * 0.5
    pdf.set_xy(0, text_y)
    pdf.cell(pdf.w, 10, name, align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
