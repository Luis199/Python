
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """This method takes in an item and inserts it into the zero index of the list
        The runtime is O(n) because inserting into the zero index forces the other indexis 
        to move """
        self.items.insert(0, item)

    def dequeue(self):

        """This methods removes the front most item from the list. 
        the runtime for this operation is O(1)"""
    
        if self.items:
            return self.items.pop()
        return None 

    def peek(self):
        """The peek method returns the last item in the list which represents the front-most 
        item in the list
        The runtime is O(1)"""
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the size of the list. 
        The runtime for this is also O(1)"""
        return len(self.items)

    def is_empty(self):
        """Returns a boolean value stating whether or not the list is empty"""
        return self.items == []


my_q = Queue()
my_q.enqueue("Luis")
my_q.enqueue("Apple")
my_q.dequeue()


print(my_q.is_empty())