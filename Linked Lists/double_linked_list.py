import random

class dnode:
	def __init__(self, data = None):
		self.data = data
		self.next = None
		self.prev = None

class dlinked_list:
	def __init__(self, first = None):
		self.head = first
		self.tail = first

	def append(self, data):
		new = dnode(data)
		self.tail.next = new
		new.prev = self.tail 
		self.tail = new

	def append_multiple(self, *data):
		for d in data:
			self.append(d)
	
	def append_multiple_randoms(self, anz, limit):
		for i in range(anz):
			self.append(int(random.random()*limit))

	# fehlt noch
	def insert(self, pos, data):
		cur = self.tail if pos > self.length()//2 else self.head
		steps = pos if True else self.length()-pos
		for i in range(steps):
			if cur == self.tail: cur = cur.prev
			else: cur = cur.next
	
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

	# in der else muss das noch adaptiert werden - wenn es am ende gelöscht wird
	# wenn pos größer als die Hälfte - von hinten, sonst von vorne anfangen
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

	# muss auch noch adaptiert werden
	def reverse(self):
		if self.length() != 0 and self.length() != 1: 
			prev = None
			cur = self.head
			while cur != None:
				next = cur.next
				cur.next = prev
				prev = cur
				cur = next
			self.head = prev

	def clear(self):
		self.head = None
		self.tail = None

	# je nach pos von hinten oder vorne anfangen
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

	