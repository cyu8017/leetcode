# LeetCode 3876 - Construct Uniform Parity Array II
# https://leetcode.com/problems/construct-uniform-parity-array-ii/

# @param {Integer[]} nums1
# @return {Boolean}
def uniform_array(nums1)
  mn = Float::INFINITY
  nums1.each { |x| mn = x if x.odd? && x < mn }
  nums1.each { |x| return false if x.even? && mn != Float::INFINITY && x < mn }
  true
end
