#Email Marketing Performance

emails = int(input('Enter Emails: '))
delivery = int(input('Enter Delivered Emails: '))
opens = int(input('Enter opened emails: '))
clicks = int(input('Enter clicked emails: '))

delivery_rate = int((delivery / emails) * 100)
open_rate = int((opens / emails) * 100)
click_rate = int((clicks / emails) * 100)
print("Delivery Rate is: "+ str(delivery_rate) + " %")
print("Open Rate is: " + str(open_rate) + " %")
print("Click Rate is: " + str(click_rate) + " %")
