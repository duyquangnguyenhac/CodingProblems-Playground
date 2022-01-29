# LC 931
# Note: Straightforward implementation of memoizing best paths. Had some issues with setting the base cases correctly to infinity not 0.

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(columns):
            dp[0][i] = matrix[0][i]
        for i in range(1, rows):
            for j in range(columns):
                upperLeft, upperRight, upperMid = float('inf'), float('inf'), float('inf')
                if j - 1 >= 0:
                    upperLeft = dp[i - 1][j - 1]
                if j + 1 < columns:
                    upperRight = dp[i - 1][j + 1]
                upperMid = dp[i - 1][j]
                dp[i][j] = min(upperLeft, upperRight, upperMid) + matrix[i][j]
        minPathSum = float('inf')
        for i in range(columns):
            minPathSum = min(minPathSum, dp[rows - 1][i])
        return minPathSum