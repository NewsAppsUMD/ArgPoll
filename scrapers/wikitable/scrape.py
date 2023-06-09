import requests
from bs4 import BeautifulSoup
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# Get secrets from GitHub
email = os.environ['EMAIL']
password = os.environ['EMAIL_PASSWORD']

url = "https://en.wikipedia.org/wiki/Opinion_polling_for_the_2023_Argentine_general_election#By_political_party_2023"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find_all('table')[1] # select the second table on the page

rows = table.find_all('tr')

# extract table headers
headers = []
for th in rows[0].find_all('th'):
    if th.find('a'):
        headers.append(th.find('a')['title'])
    else:
        headers.append(th.text.strip())

# find the index of the "Pollster" column and replace it with "Polling firm"
pollster_index = headers.index("Pollster")
headers[pollster_index] = "Polling firm"

# write table headers to CSV file
with open('voting_intentions.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

# extract table data and write to CSV file
with open('voting_intentions.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

    for row in rows[1:]:
        if row.find('th'):
            data = [row.find('th').text.strip()]
        else:
            data = []
        for td in row.find_all('td'):
            if td.find('a'):
                data.append(td.find('a').get('title', td.text.strip()))
            else:
                data.append(td.text.strip())
        writer.writerow(data)

# send email
msg = MIMEMultipart()
msg['Subject'] = "Daily Voting Intentions"
msg['From'] = email
msg['To'] = email
body = "Please find attached the latest voting intentions."
msg.attach(MIMEText(body, 'plain'))

with open("voting_intentions.csv", "rb") as f:
    attach = MIMEApplication(f.read(),_subtype="csv")
    attach.add_header('Content-Disposition','attachment',filename=str("voting_intentions.csv"))
    msg.attach(attach)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
server.sendmail(email, email, msg.as_string())
server.quit()