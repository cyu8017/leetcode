# LeetCode 2765 - Longest Alternating Subarray
# https://leetcode.com/problems/longest-alternating-subarray/

# @param {Integer[]} nums
# @return {Integer}
def alternating_subarray(nums)
  ans = -1
  n = nums.length
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      expect = (j - i).even? ? -1 : 1
      break if nums[j] - nums[j - 1] != expect
      break if nums[i + 1] - nums[i] != 1
      ans = [ans, j - i + 1].max
    end
  end
  ans
end
