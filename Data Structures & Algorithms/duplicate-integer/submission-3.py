class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dublicate = False
        seen ={}
        for num in nums:
            if num in seen:
                return True
            else:
                dublicate = False
            seen[num] = True
        return dublicate
solver = Solution()
result = solver.hasDuplicate([1,2,2,4])
        