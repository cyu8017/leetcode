# LeetCode 0371 - Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/

class Solution
  def get_sum(a, b)
    mask = 0xFFFFFFFF

    while b != 0
      carry = (a & b) << 1
      a = (a ^ b) & mask
      b = carry & mask
    end

    a <= 0x7FFFFFFF ? a : ~(a ^ mask)
  end

  alias_method :getSum, :get_sum
end
