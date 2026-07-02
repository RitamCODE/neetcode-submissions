class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            if len(prices)==1:
                return 0
            profit, max, l, r = 0, 0, 0, 1
            while(l<r and r<len(prices)):
                if (prices[r]<prices[l]):
                    print("r=",+r)
                    print("l=",+l)
                    l=r
                    r+=1
                    continue
                print("r=",+r)
                print("l=",+l)
                profit = prices[r] - prices[l]
                r+=1
                if(profit>max):
                    max=profit
            
            return max

            