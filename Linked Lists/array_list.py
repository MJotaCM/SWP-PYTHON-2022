import random

# https://www.geeksforgeeks.org/list-methods-in-python/

class array_list:
    def __init__(self):
        self.list = []

    def append(self, data):
        self.list.append(data)

    def append_multiple(self, *data):
        for d in data:
            self.append(d)

    def append_multiple_randoms(self, anz, limit):
        for i in range(anz):
            self.append(int(random.random()*limit))

    def insert(self, pos, data):
        self.list.insert(pos, data)

    def insert_multiple(self, pos, data):
        i = pos
        for d in data:
            self.list.insert(i, data)
            i = i+1

    def length(self):
        return self.list.count()

    def display_data(self):
        return self.list.__str__()

    def delete(self, pos):
        self.list.pop(pos)

    def pop(self):
        self.list.pop()

    def reverse(self):
        self.list.reverse()

    def clear(self):
        self.list = []

    def get_element():
        pass

    def get_first():
        pass

    def get_last():
        pass

    def search(self, ele):
        self.list.index(ele)

    def sort(self):
        self.list.sort()

def main():
    numb = array_list()
    numb.append_multiple_randoms(10,10)
    print(numb.display_data())
    numb.reverse()
    print(numb.display_data())
    numb.sort()
    print(numb.display_data())
    

if __name__ == "__main__":
    main()

