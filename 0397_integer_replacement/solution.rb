# LeetCode 0397 - Integer Replacement
# https://leetcode.com/problems/integer-replacement/

class Solution
  def integer_replacement(n)
    steps = 0
    while n != 1
      if n.even?
        n /= 2
      elsif n == 3 || n % 4 == 1
        n -= 1
      else
        n += 1
      end
      steps += 1
    end
    steps
  end

  alias_method :integerReplacement, :integer_replacement
end
