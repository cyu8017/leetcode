# LeetCode 3732 - Maximum Product of Three Elements After One Replacement
# https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
  a = nums.sort
  n = a.length
  aa, bb, cc, dd = a[0], a[1], a[n - 2], a[n - 1]
  x = 100000
  [aa * bb * x, cc * dd * x, -aa * dd * x].max
end
