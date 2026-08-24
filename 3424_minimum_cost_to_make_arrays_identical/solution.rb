# LeetCode 3424 - Minimum Cost to Make Arrays Identical
# https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

# @param {Integer[]} arr
# @param {Integer[]} brr
# @param {Integer} k
# @return {Integer}
def min_cost(arr, brr, k)
  no_swap = 0
  (0...arr.length).each { |i| no_swap += (arr[i] - brr[i]).abs }
  a2 = arr.sort
  b2 = brr.sort
  with_swap = k
  (0...a2.length).each { |i| with_swap += (a2[i] - b2[i]).abs }
  no_swap < with_swap ? no_swap : with_swap
end
