# LRU using OrderedDict

from collections import OrderedDict

class LRU:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value

        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value
            self.cache.move_to_end(key)
                
    def display_cache(self):
        return self.cache
        

L1 = LRU(5)
L1.put("a",1)
L1.put("b",1)
L1.put("c",1)
L1.put("d",1)
L1.put("e",1)

print(L1.get("a"))
print(L1.display_cache())
L1.put("f",1)
print(L1.display_cache())

