##################### Extra Hard Starting Project ######################
import pandas
from datetime import datetime
import random
import smtplib

my_email = "simpmadi320@gmail.com"
password = "wipn qdsz tdqn hiqc"

today_tuple = (datetime.today().month, datetime.today().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as data_file:
        contents = data_file.read()
        contents = contents.replace("[NAME]",  birthdays_dict[today_tuple]["name"])

    print(birthdays_dict[today_tuple]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_dict[today_tuple]["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )



