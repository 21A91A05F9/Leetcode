class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d.keys():
                return i
            else:
                d[i]=1
        