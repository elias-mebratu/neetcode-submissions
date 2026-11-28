class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        result = []
        product = 1
        for i in range(len(nums)):
            left.append(product)
            product = product * nums[i]

        product = 1

        for i in range(len(nums) - 1, -1, -1):
            right.append(product)
            product = product * nums[i]

        right.reverse()

        for i in range(len(nums)):
            result.append(left[i] * right[i])

        return result
       