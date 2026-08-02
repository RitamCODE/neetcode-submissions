class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, m, sum = [],[], 0, 0
        for num in height:
            left.append(m)
            m=max(num,m)

        m=0
        for num in reversed(height):
            right.append(m)
            m=max(num,m)
        for i,num in enumerate(height):
            lowest = min(left[i],right[len(right)-i-1])
            sum+= (lowest-num) if num<lowest else 0
    
        return sum