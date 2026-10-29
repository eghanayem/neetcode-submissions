class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        answer = []
        hm = {}
        for str in strs:
            letters = []
            for i in range(len(alphabet)):
                letters.append(0)
                for char in str:
                    if (char == alphabet[i]):
                        letters[i] += 1
            key = tuple(letters)
            if (key in hm):
                hm[key].append(str)
            else:
                hm[key] = [str]
        for key in hm:
            answer.append(hm[key])
        return answer