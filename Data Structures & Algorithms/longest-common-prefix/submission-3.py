class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comPrefix = "";
        for i in range(1, len(strs[0]) + 1):
            for str in strs[1:]:
                if str[:i] != strs[0][:i]: return comPrefix
            comPrefix = strs[0][:i]
        return comPrefix