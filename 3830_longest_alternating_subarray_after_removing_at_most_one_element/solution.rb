# LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
# https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

# @param {Integer[]} nums
# @return {Integer}
def longest_alternating(nums)
  n = nums.length
  l1 = Array.new(n, 1)
  l2 = Array.new(n, 1)
  r1 = Array.new(n, 1)
  r2 = Array.new(n, 1)
  ans = 0
  (1...n).each do |i|
    if nums[i - 1] < nums[i]
      l1[i] = l2[i - 1] + 1
    elsif nums[i - 1] > nums[i]
      l2[i] = l1[i - 1] + 1
    end
    ans = [ans, [l1[i], l2[i]].max].max
  end
  (n - 2).downto(0) do |i|
    if nums[i + 1] > nums[i]
      r1[i] = r2[i + 1] + 1
    elsif nums[i + 1] < nums[i]
      r2[i] = r1[i + 1] + 1
    end
  end
  (1...(n - 1)).each do |i|
    if nums[i - 1] < nums[i + 1]
      ans = [ans, l2[i - 1] + r2[i + 1]].max
    elsif nums[i - 1] > nums[i + 1]
      ans = [ans, l1[i - 1] + r1[i + 1]].max
    end
  end
  ans
end
