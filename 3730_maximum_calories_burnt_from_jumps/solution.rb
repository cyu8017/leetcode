# LeetCode 3730 - Maximum Calories Burnt from Jumps
# https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

# @param {Integer[]} heights
# @return {Integer}
def max_calories_burnt(heights)
  heights = heights.sort
  ans = 0
  pre = 0
  l = 0
  r = heights.length - 1
  while l < r
    d1 = heights[r] - pre
    ans += d1 * d1
    d2 = heights[l] - heights[r]
    ans += d2 * d2
    pre = heights[l]
    l += 1
    r -= 1
  end
  d = heights[r] - pre
  ans += d * d
  ans
end
