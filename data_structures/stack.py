class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        if self.top is None:
            return None
        val = self.top.val
        self.top = self.top.next
        return val
    
    def peek(self):
        return self.top.val if self.top is not None else None

    def is_empty(self):
        return self.peek() is None

def main():
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(3)
    s.push(5)
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())
    
if __name__ == '__main__':
    main()
