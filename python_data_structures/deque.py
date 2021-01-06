class Deque:

    def  __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0,item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop() 

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        if self.items:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
       return  self.items == []
        


my_d = Deque()
my_d.add_front("Luis")
my_d.add_front("Jose")
my_d.add_rear("Juan")


print(my_d.items)