
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
		self.wallet = 0.0
	
	def say(self, sayList ):
		print( self.whatIAm + "\t> " , end='')		
		for element in sayList:
			print( element, end='')
		print()
		
	def giveAllowance(self, amount: float):
		if amount > 0:
			self.say(("I was given 💵", amount, ". Thanks!"))
		else:
			self.say(("I was given 💵", amount, ". Boo!"))
		self.wallet += amount
		self.say(("Now I have 💵", self.wallet))

class Customer(FoodTruckParticipant):
	def __init__(self, name: str):
		self.whatIAm = "😀 " + name
		self.emotion = Emotion.hungry
		self.want = ''
		self.say(("I am born!"))
		self.wallet = 0.0

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
		self.say(("I have 💵", self.wallet, " & I'm feeling ", self.emotion, " & want: ", self.want ))

	def giveMoney(self, cost: float):
		givenMoney = 0.0
		if self.wallet >= cost:
			self.say(("Here you go"))
			givenMoney = cost
			self.wallet -= givenMoney
		else:
			self.say(("I don't have enough"))
		return givenMoney

class FoodTruck(FoodTruckParticipant):
	def __init__(self, name):
		self.whatIAm = "🚛 " + name
		self.wallet = 0.0
		self.stock = {}
		self.say(("I am in business!"))
		self.readStock()
	

	def serveCustomer(self, customer: Customer, cost: float ):
		self.customerServiceWelcome( customer )
		self.transaction( customer, cost )
		self.readStock()
		
	def askForMoney(self, customer: Customer, cost: float):
		self.say(("The price is ", cost))
		tryToGetMoney = customer.giveMoney(cost)
		if tryToGetMoney >= cost:
			self.say(("Here you go"))
			customer.given( customer.want )
			self.stock[customer.want] -= 1
			self.wallet += tryToGetMoney
		else:
			self.say(("That wasn't enough"))
			customer.given('')
		
	def transaction(self, customer: Customer, cost):
		customer.say(("I want a ",customer.want))
		if customer.want in self.stock:
			if self.stock[customer.want] > 0:
				customerPreviousEmotion = customer.emotion
				self.askForMoney(customer, cost)
				if customerPreviousEmotion == Emotion.angry:
					self.say(("I'm sorry you were feeling upset, here's a deal."))
					self.transaction(customer, cost/2 )
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
		self.say(("I have 💵", self.wallet, " and stocked: ", self.stock))

	def stockUpOn(self, foodStuff: str, wantPurchase: int, cost: float ):
		self.say(("I'm stocking up on ", foodStuff, " += ", wantPurchase))
		if not foodStuff in self.stock:
			self.stock[foodStuff] = 0
		havePurchased = 0
		while	(havePurchased < wantPurchase) & ((self.wallet - cost) >= 0.0):
			self.stock[foodStuff] += 1
			self.wallet -= cost
			havePurchased += 1
		if havePurchased != wantPurchase:
			self.say(("I couldn't buy that many, so I got ", havePurchased))	
		self.readStock()
			
	def customerServiceWelcome(self, customer: Customer ):
		self.say(("Hello, how can I help you?"))		
		customer.viewMind()


#### #### #### #### ####  



bob = Customer("bob")
bob.giveAllowance(5.0)
tacoTruck = FoodTruck("tacoTruck")
tacoTruck.giveAllowance(10.0)
print("---")

tacoTruck.stockUpOn("taco", 6, 2)
print("---")

bob.wants('burger')
print("---")
tacoTruck.serveCustomer(bob, 3)
print(">> --- ")

bob.wants('taco')
print("---")
tacoTruck.serveCustomer(bob, 3)
print(">> ---")

bob.wants('taco')
print("---")
tacoTruck.serveCustomer(bob, 3)
print(">> ---")




