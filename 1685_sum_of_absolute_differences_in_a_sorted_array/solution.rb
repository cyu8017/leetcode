# LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

# @param {Integer[]} nums
# @return {Integer[]}
def get_sum_absolute_differences(nums)
  total = nums.sum
  left = 0
  n = nums.length
  nums.each_with_index.map do |x, i|
    ans = x * i - left + (total - left - x) - x * (n - i - 1)
    left += x
    ans
  end
end
