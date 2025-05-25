import pandas as pd
import smtplib
from email.mime.text import MIMEText

# Load the spreadsheet
df = pd.read_csv("data.csv")  # Make sure columns are 'Name' and 'Email'

# Email content
subject = "Founder’s Office Intern – Assignment from Build Fast With AI"
task_link = "https://docs.google.com/document/d/1MVAdn3Sp3fByrw-n0Ry"

# Your email credentials
your_email = "your_email@gmail.com"
your_password = "your_app_password"  # Use App Password if 2FA is enabled

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(your_email, your_password)

for index, row in df.iterrows():
    name = row['Name']
    email = row['Email']
    
    body = f"""Hi {name},

Thanks for your interest in the Founder’s Office Intern – Summer Internship at Build Fast With AI.

To evaluate your research, creativity, and strategic thinking — key skills for this role — we’ve prepared a short real-world assignment (estimated time: ~3 hours).  

Task Brief Doc: {task_link}

Deadline: Please submit whatever you're able to complete within the next 48 hours. Partial submissions are totally fine — we’re excited to see your approach.

If you have any questions, feel free to reach out. Looking forward to your submission!

Best regards,
Nagmani Kumar
Team - Build Fast With AI
www.buildfastwithai.com
"""

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = your_email
    msg['To'] = email

    server.sendmail(your_email, email, msg.as_string())

server.quit()
