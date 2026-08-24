# LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
# https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

# @param {Integer[]} nums
# @param {Integer} m
# @return {Integer}
def maximum_product(nums, m)
  ans = -(10**18)
  mx = -(10**18)
  mi = 10**18
  ((m - 1)...nums.length).each do |i|
    x = nums[i]
    y = nums[i - m + 1]
    mi = [mi, y].min
    mx = [mx, y].max
    ans = [ans, [x * mi, x * mx].max].max
  end
  ans
end
