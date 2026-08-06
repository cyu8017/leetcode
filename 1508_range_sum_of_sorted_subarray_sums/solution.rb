# LeetCode 1508 - Range Sum of Sorted Subarray Sums
# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

# @param {Integer[]} nums
# @param {Integer} n
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def range_sum(nums, n, left, right)
  values = []
  (0...n).each do |i|
    total = 0
    (i...n).each do |j|
      total += nums[j]
      values << total
    end
  end
  values.sort!
  values[(left - 1)...right].sum % 1_000_000_007
end
