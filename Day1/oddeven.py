def findoutoddeven(no):
	if no % 2 == 0:
		return ("no is even")
	else:
		return ("no is odd")




print ("testing ..............................")

# for each in range(1, 11):

# 	print (each , findoutoddeven(each))


var = int(input("enter no"))

print (findoutoddeven(var))