import requests
from weasyprint import HTML

def save_webpage_as_pdf(url, output_filename):
    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.content.decode('utf-8')

    # Convert HTML to PDF
    html = HTML(string=html_content, base_url=url)
    html.write_pdf(output_filename)

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Alfred_Nobel"
    output_filename = "web_to_pdf/output.pdf"

    save_webpage_as_pdf(url, output_filename)


