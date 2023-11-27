# Week 3

# Question 1

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True


# Question 2

class Solution(object):
    def minPathSum(self,grid):
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        # Initialize the dp table with the same dimensions as the grid
        dp = [[0] * cols for _ in range(rows)]

        # Fill in the first cell of the dp table
        dp[0][0] = grid[0][0]

        # Fill in the first row of the dp table
        for i in range(1, cols):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        # Fill in the first column of the dp table
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # Fill in the rest of the dp table using dynamic programming
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][cols - 1]


# Question 3

import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Initialize a dummy node and a pointer to the dummy node
        dummy = ListNode()
        pointer = dummy
        
        # Initialize a min-heap
        heap = []
        
        # Add the head of each linked list to the heap
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, head))
        
        # While the heap is not empty
        while heap:
            # Pop the node with the smallest value from the heap
            val, node = heapq.heappop(heap)
            
            # Append the popped node to the merged linked list
            pointer.next = ListNode(val)
            pointer = pointer.next
            
            # Move the pointer in the linked list of the popped node
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        
        return dummy.next

