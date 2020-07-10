# Encapsulation means the internal representation of an object is generally hidden from  the outside view 
# Single Unit(object) == data + method



# Abstraction  ===   Implementaiton Hiding 
# Encapsulation ===  Information hiding 

#Access specifier 


# __name # private memeber variable 


class Person:
	def __init__(self):
		self.name  = "Expo data"
		self.__address  = "virtual" ## private 

	def getaddress(self):		## public to access # private variable  
		return self.__address 			# __ defines the private variable  ### can be only access using the member method 


obj = Person()
print (obj.name)
#  print (obj.__address)  ## this way will not work

print (obj.getaddress())