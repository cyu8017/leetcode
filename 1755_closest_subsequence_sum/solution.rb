# LeetCode 1755 - Closest Subsequence Sum
# https://leetcode.com/problems/closest-subsequence-sum/

# @param {Integer[]} nums
# @param {Integer} goal
# @return {Integer}
def min_abs_difference(nums, goal)
  n = nums.length
  left = nums[0, n / 2]
  right = nums[n / 2..]

  sums = lambda do |arr|
    vals = [0]
    arr.each do |x|
      vals += vals.map { |v| v + x }
    end
    vals.sort
  end

  a = sums.call(left)
  b = sums.call(right)
  best = Float::INFINITY
  j = b.length - 1
  a.each do |x|
    while j > 0 && (x + b[j] - goal).abs >= (x + b[j - 1] - goal).abs
      j -= 1
    end
    diff = (x + b[j] - goal).abs
    best = diff if diff < best
  end
  best
end
