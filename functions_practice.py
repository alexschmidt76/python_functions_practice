# define functions
def hello():
    print('hello')

def pack(e1, e2, e3):
    return [e1, e2, e3]

def eat_lunch(foods):
    print(f'First I eat {foods[0]}.')
    for i in range(1, len(foods)):
        print(f'Next I eat {foods[i]}.')
    print('My lunchbox is empty!')

# test functions
hello()
print(pack(3, 2, 1))
eat_lunch(['sandwich', 'chips', 'apple'])