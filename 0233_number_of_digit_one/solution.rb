# LeetCode 0233 - Number of Digit One
# https://leetcode.com/problems/number-of-digit-one/

class Solution
  def count_digit_one(n)
    count = 0
    factor = 1
    while factor <= n
      lower = n % factor
      current = (n / factor) % 10
      higher = n / (factor * 10)
      count += case current
               when 0 then higher * factor
               when 1 then higher * factor + lower + 1
               else (higher + 1) * factor
               end
      factor *= 10
    end
    count
  end
end
