class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        arr = [0,0]
        for i,num in enumerate(nums):
            diff = target - num
            if diff in d:
                arr[0] = d[diff]
                arr[1] = i
            d[num] = i
        return arr

