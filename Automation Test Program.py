#Question 1

def find_max(numbers):
    result = numbers[0]
    for i in numbers:
        if i > result:
            result = i
    return(result)
print(find_max([1,2,4,5])) # should print 5
print(find_max([5, 2, 7, 1, 6]))# should print 7


def find_position(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1    
print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1

#Question 2

def count(input):
    dict = {}
    for i in input:
        if i not in dict:
            dict[i] = 1
        else: dict[i] += 1
    return dict
print(count(['a', 'b', 'c', 'a', 'c', 'a', 'x'])) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input): 
    dict = {}
    for i in input:
        if i['key'] in dict:
            dict[i['key']] += i['value']
        else:
            dict[i['key']] = i['value']
    return dict

input = [ 
    {'key': 'a', 'value': 3}, 
    {'key': 'b', 'value': 1}, 
    {'key': 'c', 'value': 2}, 
    {'key': 'a', 'value': 3}, 
    {'key': 'c', 'value': 5} 
    ] 

print(group_by_key(input)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
