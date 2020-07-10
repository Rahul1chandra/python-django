## multiple + form ##

# operator overloading
# method overloading 
# method overridding

class Shape:

	# def __init__(self):
	# 	pass

	def area(self, l):
		return l*l

	# def area(self, l, b, h):
	# 	return l*b*h

	# area(*args, **kwargs)

	#area(1,2,3, var1= 11, var2=12)



class Rectange(Shape):  # child class

	# method ridding area method
	def area(self, l, b, h):
		return (l*b*h)


obj = Rectange()
print (obj.area(1,2,3))


# obj = Shape()

# print ("area of square")
# print (obj.area(2))

# print ("area of rectange")
# print (obj.area(1,2,3))

###################################################################################

