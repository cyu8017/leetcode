# LeetCode 2568 - Minimum Impossible OR
# https://leetcode.com/problems/minimum-impossible-or/

# @param {Integer[]} nums
# @return {Integer}
def min_impossible_or(nums)
  s = {}
  nums.each { |x| s[x] = true }
  x = 1
  while s[x]
    x <<= 1
  end
  x
end
