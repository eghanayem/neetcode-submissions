class MyHashSet:

    def __init__(self):
        self.nums = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.nums.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            for i in range(len(self.nums)):
                if self.nums[i] == key:
                    self.nums.pop(i)
                    break

    def contains(self, key: int) -> bool:
        for i in range(len(self.nums)):
            if self.nums[i] == key:
                return True;
        return False;
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)