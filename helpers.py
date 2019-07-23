import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Email(object):
    def __init__(self, to_email, body, from_email=None, cc_email=None):
        self.__to_email = to_email
        self.__cc_email = cc_email
        self.__body = body

        if cc_email is None:
            self.__cc = False
        else:
            self.__cc = True

        if from_email is None:
            self.__from_email = 'numbers@mcmipi.xyz'
        else:
            self.__from_email = from_email

    def __convert_to_html(self):
        return '<h1>Numbers</h1></br><p>{}</p>'.format(self.__body)

    def send(self):
        message = Mail(
            from_email=self.__from_email,
            to_emails=self.__to_email,
            subject='[MCMIPIXYV] Numbers for Betting',
            html_content=self.__convert_to_html())

        if self.__cc:
            message.cc = self.__cc_email

        try:
            # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)


class Utils(object):
    @staticmethod
    def to_string(number):
        switch = {
            1: "1 Combinations",
            2: "2 Combinations",
            3: "3 Combinations",
            4: "4 Combinations",
            5: "5 Combinations"
        }
        return switch.get(number, "Invalid number")


class Numbers(object):
    def __init__(self, list_of_numbers, groups):
        self.__list_of_numbers = list_of_numbers
        self.__list_of_numbers.sort()
        self.__groups = groups

        self.__res = {}
        self.__permutate_numbers()

    def get_numbers(self):
        return self.__res

    def __permutate_numbers(self):
        start = 0
        for group in self.__groups:
            res = []
            nums = self.__list_of_numbers[start:group]
            res.append(nums)
            for n_num in range(1, group+1):
                position_for_new_n = group
                done = False
                end = group + n_num
                while not done:
                    temp = nums.copy()
                    temp[start:n_num] = self.__list_of_numbers[position_for_new_n:end]
                    temp.sort()
                    res.append(temp)

                    position_for_new_n += 1
                    end += 1
                    if position_for_new_n >= len(self.__list_of_numbers):
                        done = True
            self.__res[Utils.to_string(group)] = res


class FileReader(object):
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise Exception("File '{}' does not exist.".format(file_path))

        self.__content = []
        self.__file_path = file_path
        self.__read_file()

    def get_content(self):
        return self.__content

    def __read_file(self):
        try:
            file = open(self.__file_path, 'r')
            content = file.readline()
            file.close()
            self.__content = list(map(int, content.split(' ')))
        except IOError:
            print("Cannot read the file {}".format(self.__file_path))
            self.__content = []
