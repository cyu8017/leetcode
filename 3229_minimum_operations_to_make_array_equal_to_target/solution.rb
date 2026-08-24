# LeetCode 3229 - Minimum Operations to Make Array Equal to Target
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

# @param {Integer[]} nums
# @param {Integer[]} target
# @return {Integer}
def minimum_operations(nums, target)
  f = (target[0] - nums[0]).abs
  (1...target.length).each do |i|
    x = target[i] - nums[i]
    y = target[i - 1] - nums[i - 1]
    if x * y > 0
      d = x.abs - y.abs
      f += d if d > 0
    else
      f += x.abs
    end
  end
  f
end
