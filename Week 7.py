# Week 7

# Question 1

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        
        # Create a matrix to store lengths of longest common subsequence
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the matrix based on characters in text1 and text2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]


# Question 2

class Solution(object):
    def uniquePaths(self, m, n):
        # Initialize a matrix to store the number of unique paths
        dp = [[1] * n for _ in range(m)]

        # Calculate the number of unique paths for each cell
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


# Question 3

class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Sort the balloons by their ending points
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]

        # Check each balloon's ending point
        for i in range(1, len(points)):
            # If the current balloon starts after the previous balloon's end, a new arrow is needed
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]  # Update the ending point

        return arrows

        