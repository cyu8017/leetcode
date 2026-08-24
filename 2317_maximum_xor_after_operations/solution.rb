# LeetCode 2317 - Maximum XOR After Operations
# https://leetcode.com/problems/maximum-xor-after-operations/

# @param {Integer[]} nums
# @return {Integer}
def maximum_xor(nums)
  ans = 0
  nums.each { |x| ans |= x }
  ans
end
