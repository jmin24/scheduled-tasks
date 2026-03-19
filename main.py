import smtplib
import datetime as dt
import random
import os
import csv

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()
day_name = now.strftime("%A")
with open("quotes.txt", "r", encoding="utf-8") as quote_file:
    all_quotes = quote_file.readlines()
    random_quote = random.choice(all_quotes).strip()
with open("contacts.csv", "r", encoding="utf-8") as contacts_file:
    reader = csv.DictReader(contacts_file)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        for row in reader:
            name = row["name"]
            email = row["email"]

            message = f"""Subject:Psst
            
Dear {name},

Happy {day_name}! During the long grind here is a word of encouragement!

{random_quote}

Sincerely,
Justin
"""

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=message
                )
