# look at a temperature and figure out what state water is in - solid, liquid or gas
 

# set the temperature first - and turn our text into a number => that's what int() does

temp = int(input("Enter a temperature: "))

if temp <= 4:
	print("Water is frozen - solid")
elif temp > 4 and temp < 100:
	print("Water is liquid")
elif temp >=100:
	print("Water is a gas")
else:
	print("You didn't enter a number")		