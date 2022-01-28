# LC 518
# Knapsack Solution
# Note: Since the question is asking for combinations not permutations of coins. The outer loop is bounded to the coins array first, to make sure the combinations built by the coins are always in ascending
# coins order, which prevents double counting permutations. For example, all combinations of 1s, 1 + 1, 1 + 1 + 1, are considered before we consider 1 + 2, or 1 + 1 + 2.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for idx in range(len(coins)):
            for cur_sum in range(len(dp)):
                if coins[idx] <= cur_sum:
                    dp[cur_sum] += dp[cur_sum - coins[idx]]
        return dp[amount]

# 2-D Array Knapsack solution
# Note: In here, dp[i - 1][j] stores the previous combinations created using the previous coins. Once we move to the next coin, we are no longer considering the previous coin in continuing our combination.
# In other words, once we have built all combinations with 1s, 1 + 1, 1 + 1 + 1. The next combinations will be 1 + 1 + 2, and never 1 + 2 + 1. dp[i][j - coins[i]] are the previous combination with this
# current coin as the last coin added in the combination.

class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        n = amount + 1
        dp = [[0] * n] * m
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if coins[i] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
        return dp[m - 1][amount]