class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x = 0
        i = 1
        maxNum = max(nums)
        while x < len(nums)-1:
            temp = nums[x]
            while i < len(nums):
                temp = temp * nums[i]
                if maxNum < temp:
                    maxNum = temp
                i=i+1
            x=x+1
        return maxNum
        




        