class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """It takes an item as a parameter and it appends it to the end of the list.
        It returns nothing 
        The runtime is O(1). It happens in a constant time
        """
        self.items.append(item)

    def pop(self):
        """This method removes and returns the last item from a list which  is also the last item 
        of a stack.
        The runtime for this operation is O(1)"""
        if self.items: 
            return self.items.pop()
        return None

    def peek(self):
        """This method returns the last item in the list which also the item at the top of the stack"""
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        """This method returns the length of a list that is representing the Stack. 
        This method runs in constant time
        """
        return len(self.items)

    def is_empty(self):
        """This methods returns a boolean value describing whether or not the stack is empty.
        The run time for this operation is O(1)"""
        return self.items == []

# # # my_stack = Stack()
# # # my_stack.push("Apple")
# # # my_stack.push("Banana")
# # # # my_stack.push("Orange")



# # # print(my_stack.is_empty())

def match_symbols(symbol_str):
    
    symbol_pairs = {
        '{': '}',
        '[':']',
        '(':')'

    }

    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else:
            if my_stack.is_empty():
                return False
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
        index += 1
    if my_stack.is_empty():
        return True
    return False             


print(match_symbols("(())"))
print(match_symbols("((})"))