class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node [' + str(self.value) + ']'


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [\n' + str(current.value) + '\n'
            while current.next is not None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def num_occ(self, data):   # number of occurences in the linked list
        node = self.first
        res = 0
        while node is not None:
            if node.value == data:
                res += 1
            node = node.next
            # print "node was %s" % node.value
        print res

L = LinkedList()
L.insert(1)
L.insert(1)
L.insert(1)
L.insert(4)

print L
print L.num_occ(8)
