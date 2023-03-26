
API_KEY="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"

import openai

import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


data= pd.read_excel("C:\\Users\\Azzam\Desktop\\codeStuff\\CompanyDatabase.xlsx" )
print(data)

CompanyAddress = data.loc[0, 'Company Address']
CompanyName = data.loc[0,'Company name']
TargetEmail = data.loc[0,'Target Email']
EmployeeName = data.loc[0, 'Employee Name']
EmployeeTeam = data.loc[0,'Employee Team or sub division']
Projects = data.loc[0,'Relevant projects']


print (CompanyAddress)


openai.api_key = API_KEY
prompt = f" generate me a phishing email for {EmployeeName} who works at {CompanyName} from his new coworker working on  {Projects} with {EmployeeTeam} team. With a subject line in the form SUBJECT: "

#response = openai.Completion.create(engine="text-davinci-001", prompt=prompt,max_tokens=2000)

prompt_string = str(prompt)

print(type(prompt))
print(type(prompt_string))
messages1=[{"role":"user", "content": prompt_string}]
chat = openai.ChatCompletion.create(
     model = "gpt-3.5-turbo", messages = messages1)
reply = chat.choices[0].message.content
print(f"ChatGPT: {reply}")


filteredReply = reply.split("\n")
first_line = filteredReply[2]
filteredReply = first_line.split(":")[1]
print (first_line)


# Set up the SMTP server
#smtp_server = "smtp.gmail.com"
#smtp_port = 587  # For starttls
#smtp_username = "your_email_address@gmail.com"
#smtp_password = "your_email_password"

# Set up the email message
#sender = "your_email_address@gmail.com"
#recipient = "recipient_email_address@example.com"

reply1 = reply.split("\n")

reply1 = reply1[4:]

print(TargetEmail)
smtp_server= "smtp-relay.sendinblue.com"
smtp_port = 587
smtp_username = "teamshazam86@gmail.com"
smtp_password = "RjOJyY96t2bwFLN0"
sender = "sanankhan629@gmail.com"
recipient = TargetEmail
subject = filteredReply
body = f"\n {reply1} "


 # make a MIME object to define parts of the email
msg = MIMEMultipart()
msg['From'] = "sanankhan629@gmail.com"
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
