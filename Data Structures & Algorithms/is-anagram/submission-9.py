class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sm = {}
        tm = {}
        for char in s:
            if char in sm:
                sm.update({char: sm.get(char) + 1})
            else:
                sm.update({char: 1})
        for char in t:
            if char in tm:
                tm.update({char: tm.get(char) + 1})
            else:
                tm.update({char: 1})
        return sm == tm
