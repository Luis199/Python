class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)


#Class Calls
s = Stack()
s.push(4)
s.push('Luis')
s.push(100)
s.push("Computer Science")
s.push(2.0)
s.pop()
print(s.peek())
