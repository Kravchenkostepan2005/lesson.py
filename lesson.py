#1
import random

def square_num(nums):
    for i in nums:
        yield i * i

nums = square_num([i * i for i in range(0, 100000, 3)])
print(nums)

f = open("abc21.txt", "w")
for i in nums:
    f.write(str(i * i) + '\n')
f.close()



def square_num(nums):
    for i in nums:
        yield i * i

nums = square_num([i * i for i in range(0, 100000, 5)])
print(nums)

f = open("abc1.txt", "w")
for i in nums:
    f.write(str(i * i) + '\n')
f.close()


def square_num(nums):
    for i in nums:
        yield i * i

nums = square_num([i * i for i in range(0, 100000, 2)])
print(nums)

f = open("abc3.txt", "w")
for i in nums:
    f.write(str(i * i) + '\n')
f.close()

#2
a = random.randint(0, 100)
b = random.randint(0, 100)
def randomizer(b):
    if b == a:
        for i in range(0, 100):
            print(b)
            break
    yield a
    
#3
def generator(start, end, step):
    list_of_values = []
    i = start - step
    while start - step <= i <= end:
        i += step
        list_of_values.append(i)
        print(i)
    if end < start and step > 0:
        return None
    if end > start and step < 0:
        return None
    while start - step >= i >= end:
        i += step
        list_of_values.append(i)
        print(i)
generator(10, -10, -3)
#4
def password():
    chars = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ$#%^&*!@'
    length = input("Password length: " + "\n")
    length = int(length)
    for i in range(1000):
        password = ''
        for i in range(length):
            password += random.choice(chars)
    lower_letter = False
    digit = False
    capital_letter = False
    symbol = False
    if lower_letter and digit and capital_letter and symbol:
        password += str(random.randint(0, 9))
    yield password
