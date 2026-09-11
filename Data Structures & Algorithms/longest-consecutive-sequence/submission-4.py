class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        count = 0
        for i in nums:
            if i - 1 not in numset:
                length = 0 
                while (i + length) in numset:
                    length += 1
                count = max(length, count)
        return count
