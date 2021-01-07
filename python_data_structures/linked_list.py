class DLLNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "SLLNode object: data = {}".format(self.data)

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        """Replace the existing value with the new data parameter"""
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_previous(self):
        return self.previous
    
    def set_previous(self, new_previous):
        self.previous = new_previous
