class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        cur = self.head
        len = 0
        while cur is not None:
            len += 1
            cur = cur.next
        return len

    def insert_to_front(self, val):
        if val is None:
            return
        node = Node(val, self.head)
        self.head = node
        return node

    def append(self, val):
        if val is None:
            return
        node = Node(val)
        if self.head is None:
            self.head = node
            return node
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        return node

    def find(self, val):
        if val is None:
            return
        cur = self.head
        while cur is not None:
            if cur.val == val:
                return cur
            cur = cur.next

    def delete(self, val):
        if val is None:
            return
        if self.head is None:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        prev = self.head
        cur = self.head.next
        while cur is not None:
            if cur.val == val:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def print_list(self):
        cur = self.head
        while cur is not None:
            print(str(cur.val) + ' -> ', end = '')
            cur = cur.next
        print('None')

def main():
    singly_linked_list = SinglyLinkedList()
    for i in range(10):
        singly_linked_list.append(i)
    singly_linked_list.insert_to_front(100)
    print(len(singly_linked_list))
    singly_linked_list.print_list()
    for i in range(1, 10, 2):
        singly_linked_list.delete(i)
    print(singly_linked_list.find(5))
    print(singly_linked_list.find(6))
    singly_linked_list.print_list()

if __name__ == '__main__':
    main()