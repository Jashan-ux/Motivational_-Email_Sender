import smtplib
import random as rm
import datetime as dt

MY_EMAIL = "jashananeja777@gmail.com"
PASSWORD = "nvjkitfmqrvgaf"


from datetime import datetime as dt

today = dt.today()

weekday_number = today.weekday()


weekdays = ["Monday", "Tuesday","Wednesday", "Thursday"  , "Friday","Saturday", "Sunday"]

weekday_name = weekdays[weekday_number]


with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = rm.choice(all_quotes)

with smtplib.SMTP("smtp.gmail.com" ,587) as connection:
    connection.starttls()
    connection.login(user = MY_EMAIL ,password = PASSWORD)
    connection.sendmail(
        from_addr= MY_EMAIL ,
        to_addrs = "mehakaneja075@gmail.com" ,
        msg= f"Subject:{weekday_name} Motivation\n\n{quote}")
    
