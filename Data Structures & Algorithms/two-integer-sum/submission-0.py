class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return ([seen[target - nums[i]],i])
            seen[nums[i]] = i
            

solver = Solution()
result = solver.twoSum([1,2,3,4],7)  

        