from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
ACCOUNT_SID = 'your_acount_sid'
AUTH_TOKEN = 'your_auth_token'


def send_message(sender, to, body):
    """
        sends message
    """
    # your code here


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    send_message('whatsapp:+15017122661', 'whatsapp:+15017122662', 'Hi!')
    print("Coding complete? Click 'Check' to earn cool rewards!")
