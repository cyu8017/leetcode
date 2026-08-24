# LeetCode 2425 - Bitwise XOR of All Pairings
# https://leetcode.com/problems/bitwise-xor-of-all-pairings/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def xor_all_nums(nums1, nums2)
  ans = 0
  nums1.each { |x| ans ^= x } if nums2.length.odd?
  nums2.each { |x| ans ^= x } if nums1.length.odd?
  ans
end
