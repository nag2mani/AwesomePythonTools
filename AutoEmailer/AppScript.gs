function sendEmails() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data = sheet.getDataRange().getValues();

  const subject = "Assignment for Generative AI Testing Intern";

  const taskLink = "https://docs.google.com/document/d/1MVAdn3Sp3f";

  for (let i = 1; i < data.length; i++) { // Skip header row
    const email = data[i][0]; // Assuming Email is column A
    const name = data[i][1]; // Assuming Name is column B
    const message = `Hi ${name},

Thanks for your interest in the Generative AI Testing Intern – Summer Internship at Build Fast With AI.

To evaluate your skills in prompt engineering, tool analysis, and user experience thinking, we’ve designed a short assignment (~3 hours) around real GenAI tools.    

Task Brief Doc: ${taskLink}

Deadline: Please submit whatever you're able to complete within the next 48 hours. Partial submissions are totally fine — we’re excited to see your approach.

If you have any questions, feel free to reach out. Looking forward to your submission!

Best regards,  
Nagmani Kumar  
Team - Build Fast With AI  
www.buildfastwithai.com`;

    GmailApp.sendEmail(email, subject, message);
  }
}