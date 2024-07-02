class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        count1 = {}

       

        
        for i in range(len(nums1)):

            count1[nums1[i]] = 1 + count1.get(nums1[i],0)

        result = []

        for num in nums2:

            if num in count1 and count1[num] > 0:

                res.append(num)
                count1[num] -= 1
        
        return res


        
       

            