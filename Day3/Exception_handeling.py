## something unwanted ## not expected ##


def result(n):
	try:
		return (12//n)
	except Exception as er:
		return (er)



print (result(2))

print (result(0))


def result_raise(n):
	try:
		raise (Exception("My custom Exception "))
	except Exception as er:
		return (er)

print (result_raise(1))




def result_isinstance(n):
	try:
		if isinstance(n, int):
			return  (str(int))
		else:
			return n

	except Exception as er:
		return (er)

print (result_raise(1))


print (result_isinstance(123))

print (result_isinstance("123"))

# Exception\
# 		-- Arithmentic Exception
# 				divide by Zero
# 		-- max Recursion reached 

# 		-- conversion excpetion (ValueError)


# try:


# excpet:


# else:

# finally: