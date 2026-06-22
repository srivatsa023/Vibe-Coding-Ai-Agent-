from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report_text, filename="startup_report.pdf"):
    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph("LaunchPilot AI - Startup Launch Pack", styles["Title"])
    content.append(title)

    content.append(Spacer(1, 12))

    for line in report_text.split("\n"):
        if line.strip():
            content.append(Paragraph(line, styles["BodyText"]))

    pdf.build(content)