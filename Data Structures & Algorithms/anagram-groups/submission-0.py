class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i,s in enumerate(strs):
            s1=''.join(sorted(s)) 
            if s1 not in map: 
                map[s1] = []
            map[s1].append(s)
        
        arr=[]
        for key in map:
            arr1 = []
            for value in map[key]:
                arr1.append(value)
            arr.append(arr1)


        return arr