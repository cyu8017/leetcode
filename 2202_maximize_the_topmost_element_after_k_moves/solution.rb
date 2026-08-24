# LeetCode 2202 - Maximize the Topmost Element After K Moves
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_top(nums, k)
  n = nums.length
  return k.odd? ? -1 : nums[0] if n == 1
  return nums[0] if k == 0

  ans = -1
  limit = [k - 1, n].min
  limit.times { |i| ans = [ans, nums[i]].max }
  ans = [ans, nums[k]].max if k < n
  ans
end
