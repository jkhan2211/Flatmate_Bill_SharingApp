from fpdf import FPDF
import webbrowser
import os
class PdfReport:
    """This is a class to generate a PDF report with the flatmates' payment details."""
    def __init__(self, filename):
        self.filename = filename  # The name of the PDF file to be generated.

    def generate(self, flatmate1, flatmate2, bill):
        """This method creates a PDF report showing the payment breakdown."""
        pdf = FPDF(orientation='P', unit='pt', format='A4')  # Initialize a PDF object.
        pdf.add_page()  # Add a new page to the PDF.

        # Calculate the payment amounts for both flatmates.
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2)))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1)))

        # Add an icon to the PDF (if available).
        pdf.image("files/house.png", w=30, h=30)

        # Add the title.
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=1, align="C", ln=1)

        # Set table settings.
        pdf.set_font(family='Times', size=14)
        col_widths = [200, 200]  # Set column widths.
        row_height = 25  # Set row height.

        # Add the period row.
        pdf.cell(200, 40, txt="Period", border=0)
        pdf.cell(200, 40, txt=bill.period, border=0, ln=1)

        # Add the first flatmate's name and amount.
        pdf.cell(col_widths[0], row_height, txt=flatmate1.name, border=0, align="C")
        pdf.cell(col_widths[1], row_height, txt=flatmate1_pay, border=0, align="C", ln=1)

        # Add the second flatmate's name and amount.
        pdf.cell(col_widths[0], row_height, txt=flatmate2.name, border=0, align="C")
        pdf.cell(col_widths[1], row_height, txt=flatmate2_pay, border=0, align="C", ln=1)

        # Save the generated PDF to a file.
        pdf.output(f"files/{self.filename}")
        
        # Change directory for the file and open the file
        os.chdir("files")
        webbrowser.open(self.filename)
