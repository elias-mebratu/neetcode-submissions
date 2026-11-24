class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hastable = {}
        for i in strs:
            key = "".join(sorted(i)) 
            if key not in hastable:
                hastable[key] = []
            hastable[key].append(i)  
        return list(hastable.values())
