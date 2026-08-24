# LeetCode 2574 - Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/

# @param {Integer[]} nums
# @return {Integer[]}
def left_right_difference(nums)
  total = nums.sum
  ans = Array.new(nums.length, 0)
  left = 0
  nums.each_with_index do |x, i|
    right = total - left - x
    ans[i] = (left - right).abs
    left += x
  end
  ans
end
