"""Creating hashtable."""
table = [None]*10


def hashing_fun(x):
    """Creating hashfuction."""
    return x % 10


def insert(value):
    """Inserting value in hashtable."""
    index = hashing_fun(value)
    table[index] = value
    return table


input = int(input("Enter the value "))
print(insert(input))
print("value inserted")
