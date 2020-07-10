# 1) single Inheritance 

# 2) multi level Inheritance

# 3) multiple Inheritance

# 4) hybrid Inheritance


print ("single Inheritance") 
class Parent:
	def parentmethod(self):
		return ("inside parent method ")


class Child(Parent):
	def childmethod(self):
		return ("Inside child method")


class GrandChild(Child):
	def grardchild(self):
		return ("Inside Grandchild method")


ob = Child()
print (ob.childmethod())
print (ob.parentmethod())


print ("multi level")
ob_gc = GrandChild()
print (ob_gc.grardchild())

print (ob_gc.childmethod())

print (ob_gc.parentmethod())








print ()

print ("Multipe Inheritance")


class Vechile:
	def vechile_name(self):
		return ("vechile_name ")

class Color:
	def color(self):
		return ("pink")


class Truck(Color, Vechile):
	def getspecifications(self):
		return ("color is pink and vechile_name %s " % ("bajaj"))


truck=Truck()
print (truck.getspecifications())


### herirical inheritance ##

print ("herirical inheritance")
class Parent:
	def fun1(self):
		return ("this is inside fun1")

class Child1(Parent):
	def fun2(self):
		return ("this inside fun2")

class Child2(Parent):
	def fun3(self):
		return ("this is inside the fun3")


obch = Child1()
print (obch.fun2())
print (obch.fun1())


obch2 = Child2()
print (obch2.fun3())
print (obch2.fun1())


### Hybrid Inheritance ###  (basically combination of all the above )



class Grand_Parent:
	def fun1(self):
		return ("this inside Grnad Parent ")

class Parent1(Grand_Parent):
	def fun2(self):
		return ("this is inside the Parent1 class")



class Parent2(Grand_Parent):
	def fun3(self):
		return ("this is inside the Parent2 class")


class Child(Parent1, Parent2):
	def fun4(self):
		return ("this is inside the child class")