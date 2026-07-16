# LeetCode 0342 - Power of Four
# https://leetcode.com/problems/power-of-four/

class Solution
  def is_power_of_four(n)
    n > 0 && (n & (n - 1)).zero? && n % 3 == 1
  end

  alias_method :isPowerOfFour, :is_power_of_four
end
