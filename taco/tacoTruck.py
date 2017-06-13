
from enum import Enum

debugMode = True

class Emotion(Enum):
	angry  = 1
	hungry = 2
	happy  = 3

class Customer:
	def __init__(self):
		self.emotion = Emotion.hungry
		self.want = ''
		print("Cust: I am born!")

	
	def wants(self, foodWant: str):
		print("Cust: Do I want a", foodWant,"?")
		if self.emotion != Emotion.happy:
			self.want = foodWant
			print("Cust: yes")
		else:
			self.want = ''
			print("Cust: no")
		self.viewMind()
			
	def given(self, foodStuff: str):
		print("Cust: I was given a", foodStuff)
		if self.want == foodStuff:
			self.want = ''
		self.selfReflection()
		self.viewMind()
		
	def selfReflection(self):
		print("Cust: I am reflecting")
		switchCase = self.emotion
		if   ( switchCase == Emotion.happy  ) :
			self.emotion = Emotion.hungry
		elif ( switchCase == Emotion.hungry ) :
			if self.want == '':
				self.emotion = Emotion.happy
			else:
				self.emotion = Emotion.angry
		elif ( switchCase == Emotion.angry  ) :
			if self.want == '':
				self.emotion = Emotion.hungry
			else:
				print("I'm so mad!!")
	
	def viewMind(self):
		print("Cust:", self.emotion, "& want:", self.want )


class FoodTruck:
	def __init__(self):
		self.stock = {
			'taco'   : 5,
			'burger' : 0
		}
		print("Truck: I am in business!")


	def serveCustomer(self, customer: Customer ):
		#print( self.stock[customer.want] )
		print("Truck: Customer wants",customer.want)
		if customer.want in self.stock:
			if self.stock[customer.want] > 0:
				print("Truck: here you go")
				self.stock[customer.want] -= 1
				customer.given(customer.want)
			else:
				print("Truck: I'm sold out of", customer.want)
				customer.given('')
		elif customer.want == '':
			print("Truck: You didn't ask for anything")
		else:
			print("Truck: I don't have any of that")
			
		self.viewMind()
	
	def viewMind(self):
		print("Truck: I have ",self.stock)



bob = Customer()
tacoTruck = FoodTruck()
print("---")

bob.wants('burger')
print("---")
tacoTruck.serveCustomer(bob)
print("---")

bob.wants('taco')
print("---")
tacoTruck.serveCustomer(bob)
print("---")

bob.wants('taco')
print("---")
tacoTruck.serveCustomer(bob)
print("---")

bob.wants('taco')
print("---")
tacoTruck.serveCustomer(bob)
print("---")