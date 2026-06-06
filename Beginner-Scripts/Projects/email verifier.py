
#email list
emails = ['user@gmail.com', 'spam_bot', 'hello@tahoo.com', 'invalid_input', 'test@outlook.com']
verified = []
Scam = []
# in the list if an email has a '@'
for email in emails:
    if '@' in email:
# put it into the verified box
        verified.append(email)
# print it out
        print('verified:', verified)
# in the list if an email has no '@'
for email in emails:
    if '_' in email:
# put it into the scam box
        Scam.append(email)
# print it out
        print('Scam:', Scam)

