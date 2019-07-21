from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Email(object):
    def __init__(self, to_email, body, from_email=None):
        self.__to_email = to_email
        self.__body = body

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

        try:
            # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)


class Numbers(object):
    def __init__(self, list_of_numbers, group):
        self.__list_of_numbers = list_of_numbers
        self.group = group

        self.res = []
        self.__permutate_numbers()

    def get_numbers(self):
        return self.res

    def __permutate_numbers(self):
        start = 0
        end = self.group
        ns = self.__list_of_numbers[start:end]
        self.res.append(ns)

        position_for_new_n = end
        done = False
        item = start
        while not done:
            temp = ns.copy()
            temp[item] = self.__list_of_numbers[position_for_new_n]
            self.res.append(temp)

            if item % self.group == 0:
                item = 0
                position_for_new_n += 1
            if position_for_new_n == len(self.__list_of_numbers):
                done = True

        return self.res


if __name__ == '__main__':
    ns = [1, 2, 3, 4, 5, 6, 7, 8]
    sets = 3
    numbers = Numbers(list_of_numbers=ns, group=sets)

    print(numbers.get_numbers())
