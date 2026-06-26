class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r =0, len(heights)-1
        max,vol = 0,0
        while(l<r):
            if heights[l]<heights[r]:
                vol = heights[l] * (r-l)
                l+=1
                # print("vol-l=",vol)
            else:
                # print("heights=",heights[r])
                # print("r=",r)
                # print("l=",l)
                vol = heights[r] * (r-l)
                r-=1
                # print("vol-r=",vol)
            
            if vol>max:
                max=vol
        
        return max