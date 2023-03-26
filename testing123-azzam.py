
API_KEY="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"

import openai

import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


data= pd.read_excel("./CompanyDatabase.xlsx" )

CompanyAddress = data.loc[0, 'Company Address']
CompanyName = data.loc[0,'Company name']
TargetEmail = data.loc[0,'Target Email']
EmployeeName = data.loc[0, 'Employee Name']
EmployeeTeam = data.loc[0,'Employee Team or sub division']
Projects = data.loc[0,'Relevant projects']
Colleague = data.loc[0,'Colleague']



openai.api_key = API_KEY
prompt = (f"Generate me a phishing email for {EmployeeName} who works at {CompanyName} with his new coworker {Colleague} working on  {Projects} with {EmployeeTeam} team."
" Also include a subject line in the form 'Subject:' on top of the email."
" Do not include any fake attachments, Malicious Link, extra names or fake email addresses.")

prompt_string = str(prompt)


messages1=[{"role":"user", "content": prompt_string}]
chat = openai.ChatCompletion.create(
     model = "gpt-3.5-turbo", messages = messages1)
reply = chat.choices[0].message.content
print(reply)


filteredReply = reply.split("\n")
first_line = filteredReply[0]
filteredReply = first_line.split(":")[1]
filteredReply = filteredReply.strip()
print (filteredReply)


# # Set up the SMTP server
# smtp_server = "smtp.gmail.com"
# smtp_port = 587  # For starttls
# smtp_username = "your_email_address@gmail.com"
# smtp_password = "your_email_password"

# # Set up the email message
# sender = "your_email_address@gmail.com"
# recipient = "recipient_email_address@example.com"

reply_temp = reply.split("\n")
reply1 = []
for x in reply1:
    if x != '':
        reply1.append(x)

reply1 = reply1[1:]
with open("output.txt","w") as text_file:
    for item in reply_temp:
        # write each item on a new line
        text_file.write("%s\n" % item)
    text_file.close
file=open("output.txt","r")
data = file.read().splitlines(True)


smtp_server= "smtp-relay.sendinblue.com"
smtp_port = 587
smtp_username = "teamshazam86@gmail.com"
smtp_password = "RjOJyY96t2bwFLN0"
sender = "teamshazam86@gmail.com"
recipient = TargetEmail
subject = filteredReply
body = ' '.join(data[1:])


 # make a MIME object to define parts of the email
msg = MIMEMultipart()
msg['From'] = "teamshazam86@gmail.com"
msg['To'] =  TargetEmail
msg['Subject'] = subject

# Attach the body of the message
msg.attach(MIMEText(body, 'plain'))
 # Cast as string
text = msg.as_string()


# message = f"""
# From: {sender}
# To: {recipient}
# Subject: {subject}

# {body}
# """

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender, recipient, text)

print("Email sent successfully!")