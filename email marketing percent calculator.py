emails = int(input('Enter the number of Sent Emails: '))
delivery = int(input('Enter the number of Delivered Emails: '))
opens = int(input('Enter the number of opened emails: '))
clicks = int(input('Enter the number of clicked emails: '))

delivery_rate = (delivery / emails) * 100
open_rate = (opens / emails) * 100
click_rate = (clicks / emails) * 100
print(delivery_rate)
print(open_rate)
print(click_rate)

