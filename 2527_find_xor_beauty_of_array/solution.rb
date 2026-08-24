# LeetCode 2527 - Find Xor-Beauty of Array
# https://leetcode.com/problems/find-xor-beauty-of-array/

# @param {Integer[]} nums
# @return {Integer}
def xor_beauty(nums)
  ans = 0
  nums.each { |x| ans ^= x }
  ans
end
