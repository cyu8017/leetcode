# LeetCode 1588 - Sum of All Odd Length Subarrays
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

# @param {Integer[]} arr
# @return {Integer}
def sum_odd_length_subarrays(arr)
  n = arr.length
  arr.each_with_index.sum { |x, i| x * (((i + 1) * (n - i) + 1) / 2) }
end
