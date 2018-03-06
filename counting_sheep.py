"""Counting Sheep
"""
DIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def CountingSheep(digit):
    """function checking the counting sleep
    """
    digits = []
    for index in range(1, 100000, 1):
        number = str(index*digit)
        number = list(number)
        for num in number:
            if not num in digits:
                digits.append(num)
        digits.sort()
        if digits == DIGIT:
            return number
    return "INSOMNIA"

counter = 0
IN_FILE = open("A-large-practice.in", 'r')
OUT_FILE = open("A-large-practice.out", 'w')
CONTENT = IN_FILE.readlines()
IN_FILE.close()
TEST = int(CONTENT[0])
CONTENT = CONTENT[1:]
print(CONTENT)
for line in CONTENT:
    counter = counter+1
    count = CountingSheep(int(line))
    OUT_FILE.write("Case #{}: {}".format(counter, ''.join(count)))
    OUT_FILE.write("\n")
OUT_FILE.close()
