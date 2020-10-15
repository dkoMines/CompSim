verbose = True

class Event:
	def __init__(self, atTime, tp):
		self.atTime = atTime
		self.tp = tp
		if (verbose):
			print(f'Creating new event. t: {int(atTime)} Type: {tp}')
	count = 0
	def __lt__(self,other):
		if self.atTime < other.atTime:
			return True
		return False

	def __str__(self):
		return f'E: {self.tp}, t: {self.atTime}'

def exponential(n):
	return n

def geometric(n):
	return n


def runSIS(s,S):
	# initialize
	eventList = []
	t = 0
	t_i = 1000

	inventory = S
	onOrder = 0

	backorderCount = 0
	orderCount = 0

	newReview = Event(7,"ReviewEvent")
	eventList.append(newReview)

	firstDemand = Event(exponential(2/3),"DemandEvent")
	eventList.append(firstDemand)

	while (len(eventList) > 0):
		eventList.sort() # Sort by atTime
		currentEvent = eventList[0]
		eventList.pop(0) # Was not in pseudo code but I think it is needed.
		t = currentEvent.atTime
		if (currentEvent.tp == "ReviewEvent"):
			nextReview = Event(t+7,"ReviewEvent")
			if (nextReview.atTime<t_i):
				eventList.append(nextReview)
			if (inventory+onOrder<=s):
				deliveryEvent = Event(t+exponential(7),"DeilveryEvent")
				deliveryEvent.count = S-(inventory+onOrder)
				onOrder += deliveryEvent.count
				eventList.append(deliveryEvent)
				orderCount += 1
		elif (currentEvent.tp == "DeilveryEvent"):
			onOrder -= currentEvent.count
			inventory += currentEvent.count
		elif (currentEvent.tp == "DemandEvent"):
			nextDemand = Event(t+exponential(2/3),"DemandEvent")
			if (nextDemand.atTime < t_i):
				eventList.append(nextDemand)
			purchased = geometric(3/4)
			if (purchased > 0):
				if (inventory >= purchased):
					inventory -= purchased
				else:
					if (inventory > 0):
						purchased -= inventory
						inventory = 0
					inventory -= purchased
					backorderCount += purchased
	if (inventory<S):
		if (inventory<0):
			backorderCount += abs(inventory)  
		orderCount += 1
		t += exponential(7)
	print(f'Time = {t} Orders = {orderCount} Back Orders = {backorderCount}')
	# Terminate



runSIS(20,80)