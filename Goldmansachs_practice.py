x = "GGGGGrrrrrrrrrrrrtdr"
UNIQUE_WORDS = []
FINAL_STRING = ""
def uniquewords(x):
    for index in x:
        if not index in UNIQUE_WORDS:
            UNIQUE_WORDS.append(index)
uniquewords(x)

COUNT = {}
for index in x:
    if index in COUNT:
        COUNT[index] += 1
    else:
        COUNT[index] = 1

def findcount(count,uniqueword):
    return count[uniqueword]

for index in UNIQUE_WORDS:
    VALUE = findcount(COUNT, index)
    FINAL_STRING = FINAL_STRING+index+""+str(VALUE)

print(FINAL_STRING)
