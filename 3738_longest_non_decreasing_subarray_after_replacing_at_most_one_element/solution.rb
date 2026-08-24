# LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
# https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

# @param {Integer[]} nums
# @return {Integer}
def longest_subarray(nums)
  n = nums.length
  left = Array.new(n, 1)
  right = Array.new(n, 1)
  (1...n).each { |i| left[i] = left[i - 1] + 1 if nums[i] >= nums[i - 1] }
  (n - 2).downto(0) { |i| right[i] = right[i + 1] + 1 if nums[i] <= nums[i + 1] }
  ans = left.max
  (0...n).each do |i|
    a = i > 0 ? left[i - 1] : 0
    b = i + 1 < n ? right[i + 1] : 0
    if i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1]
      ans = [ans, a + 1, b + 1].max
    else
      ans = [ans, a + b + 1].max
    end
  end
  ans
end
