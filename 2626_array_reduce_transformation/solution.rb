# LeetCode 2626 - Array Reduce Transformation
# https://leetcode.com/problems/array-reduce-transformation/

# @param {Integer[]} nums
# @param {Proc} fn
# @param {Object} init
# @return {Object}
def reduce(nums, fn, init)
  acc = init
  nums.each { |x| acc = fn.call(acc, x) }
  acc
end
