class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, s = 1,1
        prefix, suffix, product = [],[],[]
        for i in range(0,len(nums)-1,1):
            prefix.append(p)
            p = p*nums[i]
            
        prefix.append(p) 
        print(prefix) 
        
        for i in range(len(nums)-1,-1,-1):
            print(i)
            suffix.append(s)
            product.append(prefix[i]*s)
            s=s*nums[i]

        
        product.reverse()
        return product


        