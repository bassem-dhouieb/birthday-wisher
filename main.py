##################### Extra Hard Starting Project ######################
import pandas
import datetime
import random
import smtplib

my_email = "your@email.com"
password = "yourPassword"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
month = datetime.datetime.now().month
day = datetime.datetime.now().day
data = pandas.read_csv("birthdays.csv")
today_birthday = [[ rows.Name,rows.email, rows.year, rows.month, rows.day] for (index, rows) in data.iterrows() if
                  (rows.month == month) and (rows.day == day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for person in today_birthday:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        msg="Subject:Happy Birthday!\n\n"+letter.read().replace("[NAME]",person[0])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs=person[1],msg=msg)

