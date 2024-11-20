import collections
from Bibliotecas import mylibrary
import random


queue = collections.deque()
d = collections.OrderedDict()

Banana = "AHAHAHAHAHAHA"

mylibrary.sayHello(Banana)

value = random.random()

choices = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]

values = random.choice(choices)
print(values)

for i in range(0, 10):
    random.shuffle(choices)
    print(choices)