class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for char in s:
            if char.isalnum():
                s1 += char.lower()
        
        l, r = 0,len(s1)-1
        while(l<r):
            if s1[l] == s1[r]:
                l+=1
                r-=1
            else:
                return False
        
        return True
        