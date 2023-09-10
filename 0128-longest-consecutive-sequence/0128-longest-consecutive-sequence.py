class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_array = set(nums)

        longest = 0
        
        for n in num_array:
            if (n - 1)  not in num_array:
                length = 0
                while (n + length) in num_array:
                    length += 1

                    longest = max(length, longest)
        return longest