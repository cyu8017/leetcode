# LeetCode 0231 - Power of Two
# https://leetcode.com/problems/power-of-two/

class Solution
  def is_power_of_two(n)
    n > 0 && (n & (n - 1)).zero?
  end
end
