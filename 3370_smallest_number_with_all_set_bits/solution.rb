# LeetCode 3370 - Smallest Number With All Set Bits
# https://leetcode.com/problems/smallest-number-with-all-set-bits/

# @param {Integer} n
# @return {Integer}
def smallest_number(n)
  x = 1
  x = x * 2 + 1 while x < n
  x
end
