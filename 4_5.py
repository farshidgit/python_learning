# Converting an Integer to a String in Any Base
def num_convertor(num, base):
    if num < base:
        return str(num)
    else:
        rem = num % base
        num = num // base
        return num_convertor(num, base) + str(rem)


print num_convertor(20, 4)

