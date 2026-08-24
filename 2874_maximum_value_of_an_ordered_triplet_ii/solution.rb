# LeetCode 2874 - Maximum Value of an Ordered Triplet II
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

# @param {Integer[]} nums
# @return {Integer}
def maximum_triplet_value(nums)
  ans = 0
  max_i = 0
  max_diff = 0
  nums.each do |v|
    ans = max_diff * v if max_diff * v > ans
    max_diff = max_i - v if max_i - v > max_diff
    max_i = v if v > max_i
  end
  ans
end
