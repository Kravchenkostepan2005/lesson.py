import random

def square_num(nums):
    for i in nums:
        yield i * i

nums = square_num([i * i for i in range(0, 100000, 3)])
print(nums)

for element in nums:
    print(element)

f = open("abc2.txt", "w")
for i in nums:
    f.write(i * i + '\n')
f.close()



def square_num(nums):
    for i in nums:
        yield i * i

nums = square_num([i * i for i in range(0, 100000, 5)])
print(nums)

for element in nums:
    print(element)

f = open("abc2.txt", "w")
for i in nums:
    f.write(i * i + '\n')
f.close()


def square_num(nums):
    for i in nums:
        yield i * i

nums = square_num([i * i for i in range(0, 100000, 2)])
print(nums)

for element in nums:
    print(element)

f = open("abc2.txt", "w")
for i in nums:
    f.write(i * i + '\n')
f.close()

def randomizer(a):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    for i in range(0, 100):
        if b == a:
            print(a)
            break
    yield a


def generator(start, end, step):
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    step = int(input("Enter step: "))
    if start > end:
        print("Wrong input")
    if start < end:
        yield [start, (start + step), (start + 2 * step), (start + 3 * step)]


import random
def password(pas):
    for i in range(1000):
        pas = ''
        for x in range(16):
            pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
            print('Hello, ', num, 'your password is: ', pas)
            yield pas
