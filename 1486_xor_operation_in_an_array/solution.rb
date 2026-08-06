# LeetCode 1486 - Xor Operation In An Array
# https://leetcode.com/problems/xor-operation-in-an-array/

def xor_operation(n, start)
  ans = 0
  n.times { |i| ans ^= start + 2 * i }
  ans
end
