from twilio.rest import Client

account_sid = 'AC2603280c09aec300a82e5a1d735bac03'
auth_token = 'a6e0a4085d6ce450fc81ada7dcd0332b'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12068950458',
    body='sivan sent you a message from Python XD !',
    to='+972522922889'
)

print(message.sid)