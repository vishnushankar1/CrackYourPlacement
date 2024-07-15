class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict1=defaultdict(int)
        for i in nums:
            dict1[i]=dict1[i]+1
        for key,value in dict1.items():
            if value!=1:
                return key