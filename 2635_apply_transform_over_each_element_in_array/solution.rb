# LeetCode 2635 - Apply Transform Over Each Element in Array
# https://leetcode.com/problems/apply-transform-over-each-element-in-array/

# @param {Object[]} arr
# @param {Proc} fn
# @return {Object[]}
def map(arr, fn)
  out = Array.new(arr.length)
  arr.each_index { |i| out[i] = fn.call(arr[i], i) }
  out
end
