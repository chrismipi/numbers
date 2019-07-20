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
    def __init__(self, list_of_numbers, list_of_sets):
        self.__list_of_numbers = list_of_numbers
        self.list_of_sets = list_of_sets

    def get_sets_and_numbers(self):
        ##todo generate the sets and return them
        res = {}
        for set_item in self.list_of_sets:
            res[set_item] = [2, 3, 4, 5, 12]
        return res
