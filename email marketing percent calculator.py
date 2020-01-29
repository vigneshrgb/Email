emails = int(input('Enter Emails: '))
delivery = int(input('Enter Delivered Emails: '))
opens = int(input('Enter opened emails: '))
clicks = int(input('Enter clicked emails: '))

delivery_rate = (delivery / emails) * 100
open_rate = (opens / emails) * 100
click_rate = (clicks / emails) * 100
print(delivery_rate)
print(open_rate)
print(click_rate)

