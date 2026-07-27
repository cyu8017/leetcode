# LeetCode 1658 - Minimum Operations to Reduce X to Zero
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def min_operations(nums, x)
  target = nums.sum - x
  return -1 if target.negative?

  best = -1
  left = 0
  cur = 0
  nums.each_with_index do |v, right|
    cur += v
    while cur > target
      cur -= nums[left]
      left += 1
    end
    best = [best, right - left + 1].max if cur == target
  end
  best.negative? ? -1 : nums.length - best
end
