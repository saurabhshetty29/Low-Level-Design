#MyHashMap

class MyHashMap:
    def __init__(self, capacity=1000):
        self.table = [None] * capacity
        self.capacity = capacity
    
    def hash(self, key):
        return key % self.capacity
    
    def get(self, key):
        index = self.hash(key)
        if self.table[index] is not None and self.table[index][0] == key:
            return self.table[index][1]
        return -1
  
    def put(self, key, value):
        index = self.hash(key)
        self.table[index] = (key, value)
    
    def display_table(self):
        return self.table
    
    def remove(self, key):
        index = self.hash(key)
        if self.table[index] is not None and self.table[index][0] == key:
            self.table[index] = None


L1 = MyHashMap(1000)
L1.put(1, "S")
L1.put(2, "A")
L1.put(3, "U")
L1.put(4, "R")
L1.put(4, "A")
L1.put(4, "B")
L1.put(4, "H")
print(L1.get(3)) #prints "U"
L1.remove(3)
print(L1.get(3)) #prints -1
#print(L1.display_table())