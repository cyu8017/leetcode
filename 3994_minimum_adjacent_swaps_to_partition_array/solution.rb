# LeetCode 3994 - Minimum Adjacent Swaps to Partition Array
# https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/

# @param {Integer[]} nums
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def min_adjacent_swaps(nums, a, b)
  mod = 1_000_000_007
  result = 0
  cnt1 = 0
  cnt2 = 0
  nums.each do |x|
    if x < a
      result = (result + cnt1 + cnt2) % mod
    elsif x <= b
      cnt1 += 1
      result = (result + cnt2) % mod
    else
      cnt2 += 1
    end
  end
  result
end
