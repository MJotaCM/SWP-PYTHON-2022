import random

#https://realpython.com/linked-lists-python/

class snode:
	def __init__(self, data = None):
		self.data = data
		self.next = None


class slinked_list:
	def __init__(self, head = None):
		self.head = head
	
	def append(self, data):
		new = snode(data)
		cur = self.head
		if cur != None:
			while cur.next != None:
				cur = cur.next
			cur.next = new
		else: self.head = new

	def append_multiple(self, *data):
		for d in data:
			self.append(d)
	
	def append_multiple_randoms(self, anz, limit):
		for i in range(anz):
			self.append(int(random.random()*limit))

	def insert(self, pos, data):
		if pos > self.length(): return False 
	
		new = snode(data)
		if pos == 0:
			new.next = self.head
			self.head = new
		else:
			cur = self.head
			for i in range(0,pos-1):
				cur = cur.next
			nex = cur.next
			cur.next = new
			new.next = nex
		return True
	
	def insert_multiple(self, pos, *data):
		i = 0
		for d in data:
			i = i+1
			self.insert((pos+(i-1)),d)

	def length(self):
		cur = self.head
		l = 0
		while cur != None:
			l +=1
			cur = cur.next
		return l

	def display_data(self):
		e = []
		cur = self.head
		while cur != None:
			e.append(cur.data)
			cur = cur.next
		print(e)

	def delete(self, pos):
		if pos > self.length(): return False
		if pos == 0: 
			self.head = self.head.next
		else:
			cur = self.head
			for i in range(0,pos-1):
				cur = cur.next
			cur.next = (cur.next).next
		return True

	def pop(self):
		self.delete(self.length()-1) 

	def reverse(self):
		if self.length() != 0 and self.length() != 1: 
			prev = None
			current = self.head
			while(current is not None):
				next = current.next
				current.next = prev
				prev = current
				current = next
			self.head = prev

	def clear(self):
		self.head = None

	def get_element(self, pos):
		if pos == 0: return self.head.data
		cur = self.head
		for i in range(0,pos):
			cur = cur.next
		return cur.data

	def get_first(self):
		return self.get_element(0)

	def get_last(self):
		return self.get_element(self.length()-1)

	def search(self,ele):
		cur = self.head
		for i in range(self.length()-1):
			if cur.data == ele: return i
			cur = cur.next 
		return None

	def sort(self):
		pass

def main():
	#n = snode(2)
	slist = slinked_list()
	#slist.append(1)
	#slist.append(4)
	#slist.append(3)
	#print(slist.length())
	#print(slist.get_element(1))
	#slist.display_data()
	#slist.clear()
	#slist.display_data()
	slist.append_multiple_randoms(10,10)
	slist.display_data()
	#slist.reverse()
	#slist.display_data()
	#slist.append_multiple(1,2,3,4,5)
	#slist.display_data()
	#print(slist.search(2))
	#slist.insert(0,1)
	slist.insert_multiple(0,1,2,3)
	slist.display_data()

if __name__ == "__main__":
    main()