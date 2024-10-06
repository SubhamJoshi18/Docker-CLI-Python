from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from constant.FilePathConstant import container_pdf


pdf_path = container_pdf


pdf = canvas.Canvas(pdf_path, pagesize=A4)

def create_pdf_container_list(container_data):

    pdf.setTitle("Container List")


    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, 800, "Container List")


    pdf.setLineWidth(1)
    pdf.line(100, 790, 500, 790)


    pdf.setFont("Helvetica", 12)


    y_position = 760


    for idx, container in enumerate(container_data, 1):
        if y_position < 40:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y_position = 800


        pdf.drawString(100, y_position, f"{idx}. {container}")
        y_position -= 20


    pdf.save()

    print(f"PDF saved as {pdf_path}")



