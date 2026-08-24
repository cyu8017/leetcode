# LeetCode 2909 - Minimum Sum of Mountain Triplets II
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

# @param {Integer[]} nums
# @return {Integer}
def minimum_sum(nums)
  n = nums.length
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  mn = 1 << 30
  (0...n).each do |i|
    left[i] = mn
    mn = nums[i] if nums[i] < mn
  end
  mn = 1 << 30
  (n - 1).downto(0) do |i|
    right[i] = mn
    mn = nums[i] if nums[i] < mn
  end
  ans = 1 << 30
  (1...n - 1).each do |j|
    if left[j] < nums[j] && right[j] < nums[j]
      cand = left[j] + nums[j] + right[j]
      ans = cand if cand < ans
    end
  end
  ans == (1 << 30) ? -1 : ans
end
