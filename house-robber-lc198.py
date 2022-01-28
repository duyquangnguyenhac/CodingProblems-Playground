# LC 198 - House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        return dp[len(nums)]

# Note: We can optimized the dynamic programming solution by noticing how the computation realistically only require the two previous solutions memoized.

class Solution2:
    def rob(self, nums: List[int]) -> int:
        robPrevious = 0
        robPreviousPlusOne = 0
        bestValue = nums[0]
        for i in range(0, len(nums)):
            curRobValue = max(robPrevious, robPreviousPlusOne + nums[i])
            bestValue = max(curRobValue, bestValue)
            robPreviousPlusOne = robPrevious
            robPrevious = curRobValue
        return bestValue