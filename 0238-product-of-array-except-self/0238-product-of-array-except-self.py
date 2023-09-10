class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        rest = [1] * (len(nums))

        prefix = 1

        for i in range(1, len(nums)):

            rest[i] = rest[i-1] * nums[i-1]

        postfix = 1
        
        for i in range(len(nums) -1,-1,-1):

            rest[i] *= postfix

            postfix *= nums[i]
            
        return rest

