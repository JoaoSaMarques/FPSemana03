from collections import deque

def gualter():
    print("HEWO")
    
print(gualter())

def square2(array_of_values):
    ret = []
    for value in array_of_values:
        ret.append(value * value)
    return ret

def double2(array_of_values):
    ret = []
    for value in array_of_values:
        ret.append(value * 2)
    return ret

def square(value):
    return value * value

def double(value):
    return value * 2

def process(array_of_values, process_function):
    ret = []
    for value in array_of_values:
        ret.append(process_function(value))
    return ret

print(process([1, 2, 3], square))
print(process([1, 2, 3], double))

# appendleft() 1 2 3 -> [3 2 1] -> pop()
# appendright() 1 2 3 -> [1 2 3] -> pop()

queue = deque([1, 2, 3])
print(queue)

if (queue):
    value = queue.pop()
    print("Removed " + str(value) + " from queue")
else:
    print("Queue is empty")
    
print(queue)