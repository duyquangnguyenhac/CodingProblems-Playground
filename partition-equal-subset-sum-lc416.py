# LC 416 - Partition Equal Subset Sum
# Note: Knapsack solution with modifications, and base case protection.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0
        for i in range(len(nums)):
            totalSum += nums[i]
        if totalSum % 2 != 0:
            return False
        targetSum = int(totalSum % 2) + 1
        dp = [0] * (targetSum)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(len(dp)):
                if dp[j]:
                    continue
                dp[j] |= dp[j - nums[i]]
        return dp[targetSum]