"""
Author: Nagmani Kumar and ChatGpt
Date: 16th Jan 2024
"""

# steps:
# 1. pip install validate_email
# 2. pip3 install py3DNS
# 3. run this app.py


import pandas as pd
from validate_email import validate_email

# Load emails from input file
input_file = 'emailValidator/emails.xlsx'  # Adjust the filename if necessary
output_file = 'emailValidator/output.xlsx'

# Read the Excel file
data = pd.read_excel(input_file)

# Check if 'email' column exists
if 'email' not in data.columns:
    raise ValueError("The input file must have a column named 'email'.")

# List to store valid emails
valid_emails = []

# Validate each email
def is_valid_email(email):
    try:
        return validate_email(email, check_mx=True, verify=True)
    except Exception as e:
        print(f"Error validating {email}: {e}")
        return False

for email in data['email']:
    if isinstance(email, str) and is_valid_email(email):
        valid_emails.append(email)

# Create DataFrame of valid emails
valid_emails_df = pd.DataFrame(valid_emails, columns=['email'])

# Save to output file
valid_emails_df.to_excel(output_file, index=False)

print(f"Valid emails have been saved to {output_file}")
