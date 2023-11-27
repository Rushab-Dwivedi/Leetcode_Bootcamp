# Week 5

# Question 1

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_nodes = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result


# Question 2

class Solution(object):
    def topKFrequent(self, nums, k):
        # Create a frequency dictionary for elements in nums
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        # Create a list of buckets to store numbers by frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Place numbers in their respective frequency buckets
        for num, freq in freq_dict.items():
            buckets[freq].append(num)
        
        # Iterate through the buckets from the end to find the k most frequent elements
        result = []
        for bucket in reversed(buckets):
            if bucket:
                result.extend(bucket)
                if len(result) >= k:
                    return result[:k]
        
        return result[:k]


# Question 3

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.word = None

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                node = self.root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.word = word

            def search(self, word):
                node = self.root
                for char in word:
                    if char not in node.children:
                        return None
                    node = node.children[char]
                return node.word

        trie = Trie()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])
        result = set()

        def backtrack(node, r, c, board):
            char = board[r][c]
            curr_node = node.children.get(char)

            if curr_node and curr_node.word:
                result.add(curr_node.word)

            board[r][c] = "#"  # Mark the current cell as visited

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#" and board[nr][nc] in curr_node.children:
                    backtrack(curr_node, nr, nc, board)

            board[r][c] = char  # Restore the current cell

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    backtrack(trie.root, i, j, board)

        return list(result)
