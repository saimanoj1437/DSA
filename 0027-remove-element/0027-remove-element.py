class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        numb = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[numb] = nums[i]
                numb +=1

        return numb