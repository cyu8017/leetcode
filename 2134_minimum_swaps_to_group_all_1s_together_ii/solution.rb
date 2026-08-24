# LeetCode 2134 - Minimum Swaps to Group All 1's Together II
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

# @param {Integer[]} nums
# @return {Integer}
def min_swaps(nums)
  ones = nums.sum
  return 0 if ones == 0

  n = nums.length
  window = nums[0...ones].sum
  best = window
  n.times do |i|
    window -= nums[i]
    window += nums[(i + ones) % n]
    best = [best, window].max
  end
  ones - best
end
