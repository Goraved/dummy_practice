import os

from twilio.rest import Client

account_sid = os.getenv('account_sid')
auth_token = os.getenv('account_sid')
client = Client(account_sid, auth_token)

text_message = input('Please define text message for the SMS - ')
message = client.messages.create(
    from_=os.getenv('from_number'),
    body=text_message,
    to=os.getenv('to_number')
)

print(message.sid)
