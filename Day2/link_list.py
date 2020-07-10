class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkList:
	def __init__(self):
		self.head = None

	def addNode(self, value):
		if self.head  == None:
			self.head  = Node(value)

		else:
			obj = Node(value)
			obj.next = self.head
			self.head = obj


	def printLL(self):

		current = self.head
		while current:
			print (id(current), '|', current.data, id(current.next), " ", end='')
			current = current.next



		return ("__exited___")


if __name__ == '__main__':
	
	ll = LinkList()
	print (ll.head)
	
	for each in range(1, 3):
		ll.addNode(each)

	print (ll.printLL())

