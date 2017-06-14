
from enum import Enum

debugMode = True

class Emotion(Enum):
	angry  = 1
	hungry = 2
	happy  = 3
	
	def upgrade(self):
		return {
			Emotion.angry  : Emotion.hungry,
			Emotion.hungry : Emotion.happy,
			Emotion.happy  : Emotion.happy,
		}[self]

	def downgrade(self):
		return {
			Emotion.angry  : Emotion.angry,
			Emotion.hungry : Emotion.angry,
			Emotion.happy  : Emotion.hungry,
		}[self]

class FoodTruckParticipant:
	def __init__(self):
		self.whatIAm = "participant"
	
	def say(self, sayList ):
		print( self.whatIAm + "\t> " , end='')		
		for element in sayList:
			print( element, end='')
		print()

class Customer(FoodTruckParticipant):
	def __init__(self, name: str):
		self.whatIAm = "😀 " + name
		self.emotion = Emotion.hungry
		self.want = ''
		self.say(("I am born!"))

	def wants(self, foodWant: str):
		self.say(("Do I want a ", foodWant,"?"))
		if self.emotion != Emotion.happy:
			self.want = foodWant
			self.say(("Yup"))
		else:
			self.want = ''
			self.say(("Nope"))
		self.viewMind()
			
	def given(self, foodStuff: str):
		self.say(("I was given a '", foodStuff, "'"))
		if self.want == foodStuff:
			self.emotion = self.emotion.upgrade()
		else:
			self.emotion = self.emotion.downgrade()
		self.viewMind()
	
	def selfReflection(self):
		self.say(("I am reflecting"))
		switchCase = self.emotion 
		if self.emotion == Emotion.angry:
			self.say(("I'm so mad!!"))
		self.viewMind()

	def viewMind(self):
		self.say(( "I'm feeling ", self.emotion, " & want: ", self.want ))


class FoodTruck(FoodTruckParticipant):
	def __init__(self, name):
		self.whatIAm = "🚛 " + name
		self.stock = {}
		self.say(("I am in business!"))
		self.readStock()


	def serveCustomer(self, customer: Customer ):
		self.customerServiceWelcome( customer )
		self.giveTo( customer )
		self.readStock()
		
	def giveTo(self, customer: Customer):
		self.say(("Customer wants ",customer.want))
		if customer.want in self.stock:
			if self.stock[customer.want] > 0:
				customerPreviousEmotion = customer.emotion
				self.say(("here you go"))
				self.stock[customer.want] -= 1
				customer.given(customer.want)
				if customerPreviousEmotion == Emotion.angry:
					self.say(("I'm sorry you were feeling Angry, here's another"))
					self.giveTo(customer)
			else:
				self.say(("I'm sold out of ", customer.want))
				customer.given('')
		elif customer.want == '':
			self.say(("You didn't ask for anything"))
			customer.given('')
		else:
			self.say(("I don't have any of that"))
			customer.given('')
		
	def readStock(self):
		self.say(("I have ", self.stock))

	def stockUpOn(self, foodStuff: str, count: int):
		self.say(("I'm stocking up on ", foodStuff, " += ", count))
		if foodStuff in self.stock:
			self.stock[foodStuff] += count
		else:
			self.stock[foodStuff] = count
		self.readStock()
			
	def customerServiceWelcome(self, customer: Customer ):
		self.say(("Hello, how can I help you?"))		
		customer.viewMind()


#### #### #### #### ####  



bob = Customer("bob")
tacoTruck = FoodTruck("tacoTruck")
tacoTruck.stockUpOn("taco", 5)
print("---")

bob.wants('burger')
print("---")
tacoTruck.serveCustomer(bob)
print(">> --- ")

bob.wants('taco')
print("---")
tacoTruck.serveCustomer(bob)
print(">> ---")

bob.wants('taco')
print("---")
tacoTruck.serveCustomer(bob)
print(">> ---")




