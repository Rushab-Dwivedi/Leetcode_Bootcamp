# Week 4

# Question 1

class Solution(object):
    def findCenter(self, edges):
        frequency = defaultdict(int)
        
        # Count the frequency of each node in the edges
        for u, v in edges:
            frequency[u] += 1
            frequency[v] += 1
        
        n = len(edges) + 1  # Number of nodes in the graph
        
        # Find the node with a degree equal to n - 1 (the center node)
        for node, degree in frequency.items():
            if degree == n - 1:
                return node


# Question 2

class Solution(object):
    def minAddToMakeValid(self,s):
        open_count = 0  # Count of '(' needing to be balanced
        close_count = 0  # Count of ')' needing to be balanced
        
        for char in s:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    open_count -= 1
                else:
                    close_count += 1
        
        return open_count + close_count

            

# Question 3

class Solution(object):
    def shortestSubarray(self,nums, k):
        n = len(nums)
        min_length = float('inf')
        left = 0
        window_sum = 0

        for right in range(n):
            window_sum += nums[right]

            while window_sum >= k:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else -1
