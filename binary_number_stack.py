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


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        remstack.push(decNumber % 2)
        decNumber = int(decNumber // 2)

    bin_string = ""
    while not remstack.isEmpty():
        bin_string += str(remstack.pop())

    return bin_string

print divideBy2(128)


