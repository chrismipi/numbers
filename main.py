import schedule
import time
from helpers import Numbers, Email


def run_five_o_clock():
    print('Running 17:00')


def run_eleven_o_clock():
    print('Running 17:00')
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sets = [2, 3, 4, 5]
    numbers = Numbers(list_of_numbers=ns, groups=sets)

    print(numbers.get_numbers())


def run_every_minute():
    print('Running every minute')
    ns = [2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 54, 45, 23, 34, 34, 12, 45, 56]
    sets = [2, 3, 4, 5]
    numbers = Numbers(list_of_numbers=ns, groups=sets)
    print('Res ', numbers)

    # Send the email
    email = Email(to_email='christopher.mipi@gmail.com', body=numbers)
    email.send()


schedule.every().day.at("11:00").do(run_eleven_o_clock)
schedule.every().day.at("17:00").do(run_five_o_clock)

schedule.every().minute.do(run_every_minute)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)

