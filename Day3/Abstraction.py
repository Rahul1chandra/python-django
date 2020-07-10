## Abstraction meaning ## we are hinding the internal implmentations 
##  

from abc import ABC, abstractmethod


class Payement(ABC):
	def print_slip(self, amount):
		print ("purchase amount", str(amount))


	@abstractmethod # decorator    ### abstract method 
	def payment(self, amount):
		pass


class MobileWallet(Payement):
	def payment(self, amount):    ### concrete method 
		return ("paying using  the mobile MobileWallet %s"  % (str(amount)))


class UPIWallet(Payement):
	def payment(self, amount):    ### concrete method 
		return ("paying using  the UPI %s"  % (str(amount)))

mb=MobileWallet()
print (mb.payment(amount=22))


upi=UPIWallet()
print (upi.payment(amount=1000))