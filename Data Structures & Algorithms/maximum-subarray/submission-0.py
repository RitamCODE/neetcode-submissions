import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum,max = 0,-math.inf
        for i, num in enumerate(nums):
            sum+=num
            if(sum>max):
                max=sum
            if(sum<1):
                sum=0
        
        return max