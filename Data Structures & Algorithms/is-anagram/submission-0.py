class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {},{}
        for i in range (len(s)):
            if s[i] in  countS:
                countS[i] += 1
            else:
                countS[i] = 1
        for j in range (len(t)):
            if t[j] in countT:
                countT[j] +=1
            else:
                countT[j] = 1
        return sorted(s) == sorted(t)
solver = Solution()
result = solver.isAnagram("racecar","carrace")
        
