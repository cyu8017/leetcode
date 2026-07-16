# LeetCode 0357 - Count Numbers with Unique Digits
# https://leetcode.com/problems/count-numbers-with-unique-digits/

class Solution
  def count_numbers_with_unique_digits(n)
    return 1 if n.zero?

    total = 10
    unique = 9
    available = 9

    (2..n).each do |_length|
      unique *= available
      available -= 1
      total += unique
    end

    total
  end

  alias_method :countNumbersWithUniqueDigits, :count_numbers_with_unique_digits
end
