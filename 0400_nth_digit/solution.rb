# LeetCode 0400 - Nth Digit
# https://leetcode.com/problems/nth-digit/

class Solution
  def find_nth_digit(n)
    digits = 1
    count = 9
    start = 1

    while n > digits * count
      n -= digits * count
      digits += 1
      count *= 10
      start *= 10
    end

    number = start + (n - 1) / digits
    number.to_s[(n - 1) % digits].to_i
  end

  alias_method :findNthDigit, :find_nth_digit
end
