class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r =0, len(heights)-1
        max,vol = 0,0
        while(l<r):
            if heights[l]<heights[r]:
                vol = heights[l] * (r-l)
                l+=1
            else:
                vol = heights[r] * (r-l)
                r-=1
                            
            if vol>max:
                max=vol
        
        return max