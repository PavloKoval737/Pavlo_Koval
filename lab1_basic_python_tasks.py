# Task 1
l1 = [1, 2, 'a', 'b']
l2 = [1, 'a', 'b', 0, 15]
l3 = [1, 2, 'aasf', '1', '123', 123]


def filter_list(l):
    new_list = []
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list

print("Result task 1")
print(filter_list(l1))
print(filter_list(l2))
print(filter_list(l3))


# Task 2
def first_non_repeating_letter(string):
    low_string = []
    for i in string:
        low_string.append(i.lower())
    for i in string:
        if low_string.count(i.lower()) == 1:
            return i
    return ''

print("Result task 2")
print(first_non_repeating_letter('sTreSS'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('adress'))
print(first_non_repeating_letter('aaaaaa'))
print(first_non_repeating_letter('bob'))
print(first_non_repeating_letter(''))
print(first_non_repeating_letter('!?~:.,'))
print(first_non_repeating_letter('hello world'))


# Task 3
def digital_root(n):
    x = str(n)
    r = 0
    while len(x) > 1:
        r = 0
        for i in range(len(x)):
            r = r + int(x[i])
            print(int(x[i]), end=" ")
        x = str(r)
        print("|", x)
    return r

print("Result task 3")
print("result = ", digital_root(16))
print('')
print("result = ", digital_root(942))
print('')
print("result = ", digital_root(132189))
print('')
print("result = ", digital_root(493193))


# Task 4
def getPairsCount(arr, n, target):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count


arr = [1, 3, 6, 2, 2, 0, 4, 5]
n = len(arr)
target = 5
print("Result task 4")
print("Count of pairs is",
      getPairsCount(arr, n, target))


# Task 5
def sort_list_of_friends(str):
    str = str.split(';')
    result = []
    for i in str:
        i = i.upper().split(':')
        i[0], i[1] = i[1], i[0]
        result.append(i[0] + ', ' + i[1])
    result = sorted(result)
    str = ''
    for i in result:
        str += '(' + i + '),'
        str = str.strip(',')
    return str

print("Result task 5")
print('Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill')
print('')
print("result = ", sort_list_of_friends(
    'Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill'))


# Task 6
def nextBigger(n):
    arr = list(str(n))
    max_n = int("".join(sorted(arr, reverse=True)))
    min_n = sorted(arr)

    m = n

    while m <= max_n:
        m += 1
        if sorted(list(str(m))) == min_n:
            return m
    return -1

print("Result task 6")
print("result = ", nextBigger(12))
print('')
print("result = ", nextBigger(513))
print('')
print("result = ", nextBigger(2017))
print('')
print("result = ", nextBigger(9))
print('')
print("result = ", nextBigger(111))
print('')
print("result = ", nextBigger(531))


# Task 7
def int32_to_ip(int32):
    bin_string = f'{int32:b}'.rjust(32, '0')
    return '.'.join([str(int(bin_string[i:i + 8], 2)) for i in range(0, len(bin_string), 8)])

print("Result task 7")
print("2149583361 => ", int32_to_ip(2149583361))
print('')
print("32 => ", int32_to_ip(32))
print('')
print("0 => ", int32_to_ip(0))
