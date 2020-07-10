class Vechile:
	def __init__(self, name, color):
		self.name = name
		self.color = color

	def setname(self):
		pass




class Bus(Vechile):

	def __init__(self, name, color, brand):
		self.brand = brand
		Vechile.__init__(self, name, color)


	# member function 
	def getname(self):
		return self.name

	def getcolor(self):
		return self.color

	def getbrand(self):
		return self.brand




if __name__ == '__main__':
	bus_obj = Bus("xy", "red", "mercedise")


	print ("the name of the bus")
	print (bus_obj.getname())
	print ("the color of the bus")
	print (bus_obj.getcolor())




#### MRO concepts ###### (method resolution concepts )
## 
#### Diamond problem ###


		# 		class A  
		# 			m()                    


		# class B
		# 	m()          class c
		# 					m()

		# 		class D(B, C)


