# LeetCode 2634 - Filter Elements from Array
# https://leetcode.com/problems/filter-elements-from-array/

# @param {Object[]} arr
# @param {Proc} fn
# @return {Object[]}
def filter(arr, fn)
  out = []
  arr.each_with_index { |x, i| out << x if fn.call(x, i) }
  out
end
