# Week 1


# Question 1

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Question 2

class Solution(object):
    def maxArea(self,height):
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the area between the lines
            current_area = min(height[left], height[right]) * (right - left)
            
            # Update max_area if the current_area is greater
            max_area = max(max_area, current_area)
            
            # Move the pointers inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Question 3

class Solution(object):
    def maxSlidingWindow(self,nums, k):
        if not nums or k == 0:
            return []

        n = len(nums)
        max_vals = []

        for i in range(n - k + 1):
            window = nums[i:i+k]
            window.sort()
            max_vals.append(window[-1])

        return max_vals


