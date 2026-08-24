# LeetCode 2804 - Array Prototype ForEach
# https://leetcode.com/problems/array-prototype-foreach/

# @param {Object[]} arr
# @param {Proc} callback
# @param {Object} context
# @return {NilClass}
def for_each(arr, callback, context = nil)
  arr.each_with_index { |val, i| callback.call(val, i, arr) }
  nil
end
