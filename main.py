import schedule
import time
from helpers import Numbers, Email


def run_five_oclock():
    print('Running 17:00')


def run_eleven_oclock():
    print('Running 17:00')


def run_every_minute():
    print('Running every minute')
    ns = [2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 54, 45, 23, 34, 34, 12, 45, 56]
    sts = [2, 3, 4, 5]

    # Generate numbers
    numbers = Numbers(list_of_numbers=ns, list_of_sets=sts)
    results = numbers.get_sets_and_numbers()
    print('Res ', results)

    # Send the email
    email = Email(to_email='christopher.mipi@gmail.com', body=results)
    email.send()


schedule.every().day.at("11:00").do(run_eleven_oclock)
schedule.every().day.at("17:00").do(run_five_oclock)

schedule.every().minute.do(run_every_minute)

if __name__ == '__main__':

    while True:
        schedule.run_pending()
        time.sleep(1)
