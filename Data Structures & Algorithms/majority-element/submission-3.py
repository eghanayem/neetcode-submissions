class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 0
        keys = list(hm.keys())
        majorityElement = keys[0]
        majorityNumber = hm[keys[0]]
        for i in range(1, len(keys)):
            if hm[keys[i]] > majorityNumber:
                majorityNumber = hm[keys[i]]
                majorityElement = keys[i]
        return majorityElement

        