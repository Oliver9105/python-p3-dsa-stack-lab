class Stack:
    def __init__(self, items=None, limit=10):
        self.items = items if items else []
        self.limit = limit

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def full(self):
        return len(self.items) == self.limit

    def search(self, element):
        try:
            return len(self.items) - self.items.index(element)
        except ValueError:
            return -1
