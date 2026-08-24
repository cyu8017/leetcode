# LeetCode 0625 - Minimum Factorization
# https://leetcode.com/problems/minimum-factorization/

# @param {Integer} num
# @return {Integer}
def smallest_factorization(num)
  return num if num < 10

  digits = []
  9.downto(2) do |digit|
    while num % digit == 0
      digits << digit
      num /= digit
    end
  end

  return 0 if num != 1

  result = 0
  digits.reverse_each do |digit|
    result = result * 10 + digit
    return 0 if result > 2**31 - 1
  end
  result
end
