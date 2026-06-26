class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0 
        nums_set = set(nums)
        for num in nums:
            count = 1
            if num - 1 not in nums:
                # that means that num is the starting point of a sequence
                n = num
                while n + 1 in nums_set:
                    n = n+1
                    count += 1
                
                if count>max:
                    max = count

        return max