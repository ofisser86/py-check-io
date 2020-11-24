import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = 'Enter the API key here that you generated at SendGrid.com'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(API_KEY)


def send_email(email, name):
    pass


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
