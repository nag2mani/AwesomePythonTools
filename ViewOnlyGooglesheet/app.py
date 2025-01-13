import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Google Sheets preview page
# This sheet contains emails and we can't copy it manually so I have scrapped it using bs4.
url = "link_to_googlesheet/htmlview"
# url = "https://docs.google.com/spreadsheets/d/11RINwimXdBOxgIPD5c_PXuM0jmwbqpKh/htmlview"

# Send a GET request to fetch the page content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all rows in the sheet body
    rows = soup.find_all("tr")
    
    # Extract emails from rows
    emails = []
    for row in rows:
        cells = row.find_all("td")  # Find all cells in the row
        for cell in cells:
            text = cell.get_text(strip=True)
            if "@" in text and "." in text:  # Check if the cell contains an email
                emails.append(text)

    # Save emails to an Excel file
    if emails:
        df = pd.DataFrame(emails, columns=["Email"])
        df.to_excel("emails.xlsx", index=False)
        print("Emails have been saved to emails.xlsx")
    else:
        print("No emails found in the sheet.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
