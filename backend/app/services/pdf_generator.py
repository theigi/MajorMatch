import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER

def generate_report_pdf(student_data, prediction):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=LETTER)
    
    # Header
    p.setFont("Helvetica-Bold", 20)
    p.drawString(100, 750, "MajorMatch: Academic Report")
    
    # Student Data
    p.setFont("Helvetica", 12)
    p.drawString(100, 700, f"Math Score: {student_data.math}")
    p.drawString(100, 680, f"Physics Score: {student_data.physics}")
    p.drawString(100, 660, f"Chemistry Score: {student_data.chemistry}")
    p.drawString(100, 640, f"English Score: {student_data.english}")
    p.drawString(100, 620, f"Interest Area: {student_data.interest}")
    
    # Recommendation
    p.setFont("Helvetica-Bold", 14)
    p.setStrokeColorRGB(0.38, 0.4, 0.94) # MajorMatch Purple
    p.drawString(100, 580, f"Recommended Major: {prediction}")
    
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer