import smtplib
from datetime import datetime
import pandas
import random

my_email = "simpmadi320@gmail.com"
password = "wipn qdsz tdqn hiqc"

now = datetime.now()

weekday = now.weekday()
print(now)
"""
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)



        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() #Encrpyted for secure email
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg=f"Subject:Monday Motivation\n\n{quote}")
            connection.close()

"""