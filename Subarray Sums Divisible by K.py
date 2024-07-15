class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        d[0]=1
        sum1=0
        c=0
        for i in nums:
            sum1+=i
            out=sum1%k
            if out in d:
                c+=d[out]
            d[out]+=1
        print(d)
        return c