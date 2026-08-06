# LeetCode 1365 - How Many Numbers Are Smaller Than The Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smaller_numbers_than_current(nums)
  sorted = nums.sort
  nums.map { |x| sorted.index(x) }
end
