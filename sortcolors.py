class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict1=defaultdict(int)
        for i in nums:
            dict1[i]=dict1[i]+1
    
        nums1=[0]*dict1[0]+[1]*dict1[1]+[2]*dict1[2]
        for i in range(len(nums)):
            nums[i]=nums1[i]

        