# LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

# @param {Integer[]} nums
# @param {Integer} value
# @return {Integer}
def find_smallest_integer(nums, value)
  cnt = Array.new(value, 0)
  nums.each do |x|
    r = x % value
    r += value if r < 0
    cnt[r] += 1
  end
  mex = 0
  while cnt[mex % value] > 0
    cnt[mex % value] -= 1
    mex += 1
  end
  mex
end
