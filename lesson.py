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
def randomizer(a):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    for i in range(0, 100):
        if b == a:
            print(a)
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
generator(2, 12, 4)

#4
def password():
    password = random.choice('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ$#%^&*!@')
    password + str(random.randint(0, 9))
    password_list = [1, 2, 3, 4, "f", "j", "F", "L", "D", "#", "$"]

    yield password
