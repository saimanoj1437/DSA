class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        newmap = {}

        for i in range(len(nums)):

            newmap[nums[i]] = 1 + newmap.get(nums[i],0)

        print(newmap)

        new_sort = sorted(nums, key=lambda i:(newmap[i],-i))

        return new_sort