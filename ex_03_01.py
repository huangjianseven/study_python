hrs = input("Enter Hours:")

rate = input("Enter Hourly Rate:")

hrs = float(hrs)
rate = float(rate)

if hrs > 40:
	rate_new = rate * 1.5
	pay = (hrs-40)*rate_new +40*rate 
else:
	pay = hrs * rate

print(pay)
