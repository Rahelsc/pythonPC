"""
Question 4 - sending emails to a contact list asynchronously
"""

import csv
import smtplib
import os
from email.message import EmailMessage  # to send more intuitive emails.. better formatting
import time
import concurrent.futures

t1 = time.perf_counter()

# just some values to try out
details_dict = [{"first_name": "רחל", "last_name": "שורץ", "Gender": "אישה", "City": "פתח תקווה",
                 "Email": "rahelsc@gmail.com", "Relationship Status": "Married"},
                {"first_name": "דב", "last_name": "שורץ", "Gender": "גבר", "City": "פתח תקווה",
                 "Email": "37good37@gmail.com", "Relationship Status": "Single"},
                {"first_name": "רונן", "last_name": "שורץ", "Gender": "גבר", "City": "פתח תקווה",
                 "Email": "scwartz123@gmail.com", "Relationship Status": "Single"}]

# entering data into a csv file from the dict above
with open('contact_list.csv', 'w+', newline='') as contacts:  # file creation
    field_names = ['first_name', 'last_name', 'Gender', 'City', 'Email', 'Relationship Status']  # table headers

    csv_writer = csv.DictWriter(contacts, fieldnames=field_names, delimiter=',')

    csv_writer.writeheader()  # writing the header into the file

    for line in details_dict:  # looping over array to input data into the new csv file
        csv_writer.writerow(line)


def party_mail_list(contact):
    # getting email details from environmental variables (TO KEEP IT SECURE)
    EMAIL_ADDRESS = os.environ.get('EMAIL_AD')
    EMAIL_PASSWORD = os.environ.get('PYTHON_TEST')
    fname = contact['first_name']
    lname = contact['last_name']
    city = contact['City']
    r_status = contact['Relationship Status']
    bring_your_spouse = 'תביא/י את בן/ת הזוג' if r_status != 'Single' else ' '
    msg = EmailMessage()
    msg['Subject'] = 'מסיבת פייתון!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contact['Email']
    msg['Content-Type'] = "text/html; charset=UTF-8"
    msg.set_content("""\
            <!DOCTYPE html>
                <html>
                    <body dir='rtl'>
                         <h1 style="color:blue"> את/ה מוזמן/ת למסיבה בעיר מגוריך </h1>
                    </body>
                </html>

            """, subtype='html')  # backup email text

    msg.add_alternative(f'{fname} {lname} היקר\n'
                        f'את/ה מוזמן/ת למסיבה שתתקיים ב{city}\n'
                        f'{bring_your_spouse}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # for secure connection use _ssl port 465
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # using app password from google
        smtp.send_message(msg)
    return f'{contact} sent'


# creating threads and sending messages asynchronously
with concurrent.futures.ThreadPoolExecutor() as executer:
    with open('contact_list.csv', 'r') as contacts:
        csv_reader = csv.DictReader(contacts)
        results = executer.map(party_mail_list, csv_reader)

# printing the timing of results sent
        for result in results:
            print(result)

t2 = time.perf_counter()

print(f'finished in {t2 - t1} seconds')

# result when running without threads: "C:\Users\rahel\Google Drive\אריאל\שנה א\סמסטר
# ב\python\recursion\venv\Scripts\python.exe" "C:/Users/rahel/Google Drive/אריאל/שנה א/סמסטר
# ב/python/recursion/automatic_mail.py" {'first_name': 'Rahel', 'last_name': 'Schwartz', 'Gender': 'Female',
# 'City': 'Petach-tikva', 'Email': 'rahelsc@gmail.com', 'Relationship Status': 'Single'} sent {'first_name': 'Dov',
# 'last_name': 'Schwartz', 'Gender': 'Male', 'City': 'Petach-tikva', 'Email': '37good37@gmail.com', 'Relationship
# Status': 'Single'} sent {'first_name': 'Ronen', 'last_name': 'Schwartz', 'Gender': 'Male', 'City': 'Petach-tikva',
# 'Email': 'scwartz123@gmail.com', 'Relationship Status': 'Single'} sent finished in 4.6403962 seconds

# results using threads: {'first_name': 'Rahel', 'last_name': 'Schwartz', 'Gender': 'Female', 'City': 'Petach-tikva',
# 'Email': 'rahelsc@gmail.com', 'Relationship Status': 'Single'} sent {'first_name': 'Dov', 'last_name': 'Schwartz',
# 'Gender': 'Male', 'City': 'Petach-tikva', 'Email': '37good37@gmail.com', 'Relationship Status': 'Single'} sent {
# 'first_name': 'Ronen', 'last_name': 'Schwartz', 'Gender': 'Male', 'City': 'Petach-tikva',
# 'Email': 'scwartz123@gmail.com', 'Relationship Status': 'Single'} sent finished in 2.6091711 seconds
