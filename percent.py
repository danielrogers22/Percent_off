def percent_off25(price):
	price = float(price) * 0.25
	return price
def percent_off10(price):
	price = float(price) * 0.10
	return price
	
	
print "Enter a number!"
cost = float(raw_input())

print "Do you want to see 25 percent off or 10 percent off?"
number = int(raw_input())
if number == 10:
	total_off10 = percent_off10(cost)
	price_off10 = cost - total_off10
	print "Here is 10 percent off that number! \n%r" % price_off10
elif number == 25:
	total_off25 = percent_off25(cost)
	price_off25 = cost - total_off25
	print "Here is 25 percent off that number! \n%r" % price_off25
else:
		print "Sorry try again."
