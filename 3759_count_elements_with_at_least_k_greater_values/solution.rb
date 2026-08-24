# LeetCode 3759 - Count Elements with at Least K Greater Values
# https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_elements(nums, k)
  n = nums.length
  return n if k == 0
  a = nums.sort
  ans = 0
  (0...(n - k)).each { |i| ans += 1 if a[n - k] > a[i] }
  ans
end
