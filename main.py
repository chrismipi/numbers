import schedule
import time
from helpers import Numbers, Email, FileReader


def run_five_o_clock():
    print('Running 17:00')


def run_eleven_o_clock():
    print('Running 17:00')
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sets = [2, 3, 4, 5]
    numbers = Numbers(list_of_numbers=ns, groups=sets)

    print(numbers.get_numbers())


def run_every_minute():
    try:
        print('Read the file')
        file_reader = FileReader('file_sample.txt')
        nums = file_reader.get_content()

        print('Running every minute')
        sets = [2, 3, 4, 5]
        # Getting the numbers
        numbers = Numbers(list_of_numbers=nums, groups=sets)
        nums = numbers.get_numbers()

        # write to a file
        content = ''

        for k, v in nums.items():
            content += k + '\n'
            for num in v:
                content += str(num) + '\n'
            content += '\n'

        out = open('numbers.txt', 'w')
        out.write(content)
        out.close()

        # Send the email
        # email = Email(to_email='christopher.mipi@gmail.com', body=numbers, cc_email='thembidmolotsi@gmail.com')
        # email.send()

        print('Sent...')

    except Exception as ex:
        print(ex)


schedule.every().day.at("11:00").do(run_eleven_o_clock)
schedule.every().day.at("17:00").do(run_five_o_clock)

schedule.every().minute.do(run_every_minute)

if __name__ == '__main__':
    run_every_minute()

# if __name__ == '__main__':
#     try:
#         print('Starting the app')
#         while True:
#             schedule.run_pending()
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print('Stopping the app.')
#     except Exception as ex:
#         print('Something happened {}'.format(ex))
