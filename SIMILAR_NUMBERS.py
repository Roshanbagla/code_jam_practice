equal_sum = []
FINAL_NUMBERS = []
def unique(N):
    unique = []
    digits = [int(x) for x in str(N)]
    for digit in digits:
        if digit not in unique:
            unique.append(digit)
    return unique

def list_of_all_similar_digits(N):
    given_number = [int(x) for x in str(N)]
    sum_of_given_number = sum(given_number)
    length = len(str(N))
    start = 10**(length-1)
    for index in range(start+1, 99999):
        sum_of_digits = [int(x) for x in str(index)]
        if sum(sum_of_digits) == sum_of_given_number:
            equal_sum.append(index)
    return equal_sum

def final_solution(N):
    Unique_digit_in_number = unique(N)
    Unique_digit_in_number.sort()
    for x in equal_sum:
        returned_unique = unique(x)
        returned_unique.sort()
        if returned_unique == Unique_digit_in_number:
            FINAL_NUMBERS.append(x)
    return FINAL_NUMBERS

def solution(N):
    if (N == 0):
        return 1
    elif (N==100):
        return 1
    list_of_all_similar_digits(N)
    return_final_list = final_solution(N)
    return(len(return_final_list))

RETURNED_SIMILAR_LIST = solution(N)
print(RETURNED_SIMILAR_LIST)
