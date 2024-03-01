import smtplib
from datetime import datetime

"""
my_email = "simpmadi320@gmail.com"
password = "wipn qdsz tdqn hiqc"

with smtplib.SMTP("smtp.gmail.com") as connection
    connection.starttls() #Encrpyted for secure email
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="simpmadi320@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of my email.")
    connection.close()
"""

now = datetime.now()
dt = now.date()
print(dt)

date_of_birth = dt.datetime(year=2000, month=101, day=16)
print(date_of_birth)