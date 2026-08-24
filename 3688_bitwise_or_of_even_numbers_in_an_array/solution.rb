# LeetCode 3688 - Bitwise OR of Even Numbers in an Array
# https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def even_number_bitwise_o_rs(nums)
  ans = 0
  nums.each { |x| ans |= x if x.even? }
  ans
end
