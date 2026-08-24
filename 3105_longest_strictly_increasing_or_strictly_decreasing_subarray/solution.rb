# LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

# @param {Integer[]} nums
# @return {Integer}
def longest_monotonic_subarray(nums)
  ans = 1
  t = 1
  (1...nums.length).each do |i|
    if nums[i - 1] < nums[i]
      t += 1
      ans = [ans, t].max
    else
      t = 1
    end
  end
  t = 1
  (1...nums.length).each do |i|
    if nums[i - 1] > nums[i]
      t += 1
      ans = [ans, t].max
    else
      t = 1
    end
  end
  ans
end
