# Week 2


# Question 1

class Solution(object):
    def isIsomorphic(self,s, t):
        if len(s) != len(t):
            return False
        
        s_to_t = {}  # Mapping from s to t
        t_to_s = {}  # Mapping from t to s
        
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            
            # Check s to t mapping
            if s_char in s_to_t:
                if s_to_t[s_char] != t_char:
                    return False
            else:
                s_to_t[s_char] = t_char
            
            # Check t to s mapping
            if t_char in t_to_s:
                if t_to_s[t_char] != s_char:
                    return False
            else:
                t_to_s[t_char] = s_char
        
        return True


# Question 2

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        char_index = {}  # Dictionary to track characters and their indices
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            
            char_index[s[end]] = end
            max_length = max(max_length, end - start + 1)
        
        return max_length


# Question 3

class Solution(object):
    from collections import Counter

    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""

        # Count the characters in t
        t_counts = Counter(t)
        required_chars = len(t_counts)
        formed_chars = 0
        
        # Initialize window pointers and minimum window variables
        left = right = 0
        min_len = float('inf')
        min_window = ""
        
        # Dictionary to track characters in the current window
        window_counts = {}
        
        while right < len(s):
            # Expand the window to the right
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if the current character in window is in t and forms a required count
            if char in t_counts and window_counts[char] == t_counts[char]:
                formed_chars += 1
            
            # Try to shrink the window from the left
            while left <= right and formed_chars == required_chars:
                # Update the minimum window if a smaller one is found
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                
                # Reduce the window size from the left
                char = s[left]
                window_counts[char] -= 1
                if char in t_counts and window_counts[char] < t_counts[char]:
                    formed_chars -= 1
                
                left += 1
            
            # Move right pointer to expand the window
            right += 1

        return min_window
