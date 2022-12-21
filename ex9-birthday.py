import datetime

today = datetime.datetime.now()
birthday = int(input('Enter your birthday'))
year = today.year
rx = year - birthday
print('your age is : ' ,rx)