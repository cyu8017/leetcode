# LeetCode 2908 - Minimum Sum of Mountain Triplets I
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

# @param {Integer[]} nums
# @return {Integer}
def minimum_sum(nums)
  n = nums.length
  ans = 1 << 30
  (1...n - 1).each do |j|
    left = 1 << 30
    right = 1 << 30
    (0...j).each do |i|
      left = nums[i] if nums[i] < nums[j] && nums[i] < left
    end
    (j + 1...n).each do |k|
      right = nums[k] if nums[k] < nums[j] && nums[k] < right
    end
    if left < (1 << 30) && right < (1 << 30)
      cand = left + nums[j] + right
      ans = cand if cand < ans
    end
  end
  ans == (1 << 30) ? -1 : ans
end
