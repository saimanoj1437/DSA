class Solution:
    def sortColors(self, nums: List[int]) -> None:

        l,r = 0,len(nums) - 1
        i = 0
        

        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            
            if nums[i] == 0:

                swap(l,i)
                l += 1

            elif nums[i] == 2:

                swap(r,i)

                r -=1
                i -=1

            i += 1