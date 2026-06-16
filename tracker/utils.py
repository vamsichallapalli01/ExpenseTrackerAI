from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(
    total_income,
    total_expense,
    savings
):

    buffer = BytesIO()

    pdf = SimpleDocTemplate(
        buffer
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Expense Tracker Report",
            styles['Title']
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Total Income: ${total_income}",
            styles['BodyText']
        )
    )

    content.append(
        Paragraph(
            f"Total Expense: ${total_expense}",
            styles['BodyText']
        )
    )

    content.append(
        Paragraph(
            f"Savings: ${savings}",
            styles['BodyText']
        )
    )

    pdf.build(content)

    buffer.seek(0)

    return buffer