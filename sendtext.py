from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC21bdb75cd16649692c0227bb0ba2def4"
auth_token  = "5701f8e6d79afee8078d5bed696aa229"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="This is Prasad, I Love you Amma!!!",
    to="+14803266021",    # Replace with your phone number
    from_="+16237481551") # Replace with your Twilio number
print message.sid
