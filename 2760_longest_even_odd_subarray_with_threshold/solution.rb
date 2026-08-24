# LeetCode 2760 - Longest Even Odd Subarray With Threshold
# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def longest_alternating_subarray(nums, threshold)
  ans = 0
  n = nums.length
  (0...n).each do |i|
    next if nums[i].odd? || nums[i] > threshold
    j = i
    j += 1 while j + 1 < n && nums[j + 1] <= threshold && nums[j + 1] % 2 != nums[j] % 2
    ans = [ans, j - i + 1].max
  end
  ans
end
