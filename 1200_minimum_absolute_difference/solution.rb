# LeetCode 1200 - Minimum Absolute Difference
# https://leetcode.com/problems/minimum-absolute-difference/

# @param {Integer[]} arr
# @return {Integer[][]}
def minimum_abs_difference(arr)
  arr = arr.sort
  best = (0...arr.length - 1).map { |i| arr[i + 1] - arr[i] }.min
  (0...arr.length - 1).select { |i| arr[i + 1] - arr[i] == best }.map { |i| [arr[i], arr[i + 1]] }
end
