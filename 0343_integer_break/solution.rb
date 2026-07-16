# LeetCode 0343 - Integer Break
# https://leetcode.com/problems/integer-break/

class Solution
  def integer_break(n)
    return n - 1 if n <= 3

    product = 1
    while n > 4
      product *= 3
      n -= 3
    end
    product * n
  end

  alias_method :integerBreak, :integer_break
end
