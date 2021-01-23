import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "studious.estudent12345@gmail.com"
MY_PASSWORD = "8qA5Jt6e!K2S#kow"


now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

bday_read = pandas.read_csv("birthdays.csv")
bdays = bday_read.to_dict()

birthday_dict = {(data_rows.month, data_rows.day): data_rows for (index, data_rows) in bday_read.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as data:
        contents = data.read()
        new_contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="studious.estudent0@yahoo.com",
            msg=f"Subject:From Yours Dearly\n\n{new_contents}"
        )
