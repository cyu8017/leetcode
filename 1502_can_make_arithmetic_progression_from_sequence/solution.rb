# LeetCode 1502 - Can Make Arithmetic Progression From Sequence
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

# @param {Integer[]} arr
# @return {Boolean}
def can_make_arithmetic_progression(arr)
  arr = arr.sort
  diff = arr[1] - arr[0]
  (2...arr.length).all? { |i| arr[i] - arr[i - 1] == diff }
end
