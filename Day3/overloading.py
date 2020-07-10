## operator  overloading 
##  +  "first name "+ "second name"     
##      [1,2,3] + [4,5,6], etc..........


#function overloading

class Add:
	def summ(*arg, **kwargs):  ### special parement for python to holds the n no. of argument 
		sum_count = 0
		for each_no in arg:
			print (each_no)
		print (kwargs)  ### dictionry  {"var1" :"arg1", "var2": "arg2"}
		return (sum_count)




add=Add()

print (add.summ(1,2,3))

print (add.summ(1,2,3, var1= "arg1", var2="arg2"))

# print (add.summ(1,2,3,4,5,6,7,8))


