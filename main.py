import pandas
import random
import smtplib
import datetime as dt

MY_EMAIL = None # YOUR EMAIL
PASS = None # YOUR PASS
LETTERS = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

now = dt.datetime.now()
now_month = now.month
now_day = now.day

friends_data = pandas.read_csv('birthdays.csv')
friends_data_dict = {friends_data.loc[row.name, 'name']: (row.day, row.email, row.month) for (index, row)
                     in friends_data.iterrows()}

for name in friends_data_dict.keys():
    if now_month in friends_data_dict[name] and now_day in friends_data_dict[name]:
        choose_letter = random.choice(LETTERS)
        with open(choose_letter, 'r') as file:
            text_for_user = file.read().replace('[NAME]', name)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=friends_data_dict[name][1],
                msg=f'Subject: HAPPY BIRTHDAY!\n\n{text_for_user}'
            )
