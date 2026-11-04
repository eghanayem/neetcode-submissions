class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            self.map.append([key, value])
        else:
            for el in self.map:
                if el[0] == key:
                    el[1] = value
                    break

    def get(self, key: int) -> int:
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                return self.map[i][1]
        return -1  

    def remove(self, key: int) -> None:
        if self.get(key) != -1:
            for i in range(len(self.map)):
                if self.map[i][0] == key:
                    self.map.pop(i)
                    break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)