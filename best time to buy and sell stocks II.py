class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 2 for i in range(len(prices))]  
        def stock(ind,buy,n,prices):
            if ind==n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                profit=max(-prices[ind]+stock(ind+1,0,n,prices),stock(ind+1,1,n,prices))
            else:
                profit=max(prices[ind]+stock(ind+1,1,n,prices),stock(ind+1,0,n,prices))
            dp[ind][buy]=profit
            return dp[ind][buy]
        return stock(0,1,len(prices),prices)
        