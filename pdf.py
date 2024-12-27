import pdfkit
from markdown import markdown
def convert_md_to_pdf(md_file, pdf_file):
    path_to_wkhtml = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

    config = pdfkit.configuration(wkhtmltopdf= path_to_wkhtml)
    with open(md_file, 'r', encoding='utf-8') as file:
        text = file.read()
        
        html_content = markdown(text)
        pdfkit.from_string(html_content,pdf_file,configuration= config)
        return html_content

