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


def hex_convertor(dec_number):
    hex_stack = Stack()

    while dec_number > 0 :
        rem = dec_number % 16  # hexadecimal reminder
        hex_stack.push(rem)
        dec_number = dec_number // 16

    hex_rep = "" # hexadecimal representation

    def digit_convertor(digit):
        return {10: 'A',
                11: 'B',
                12: 'C',
                13: 'D',
                14: 'E',
                15: 'F',
                }[digit]

    while not hex_stack.isEmpty():
        digit = hex_stack.pop()
        if digit > 9:
            digit = digit_convertor(digit)
        else:
            digit = str(digit)

        hex_rep += digit


    return hex_rep

print hex_convertor(1498735)