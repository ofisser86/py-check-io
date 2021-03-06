import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = ''
SUBJECT = 'Welcome'


sg = sendgrid.SendGridAPIClient(API_KEY)


def send_email(email, name):
    body = f'Hi {name}'
    message = Mail(
        from_email=email,
        to_emails=email,
        subject=SUBJECT,
        plain_text_content=body)
    try:
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
