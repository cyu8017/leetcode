# LeetCode 2847 - Smallest Number With Given Digit Product
# https://leetcode.com/problems/smallest-number-with-given-digit-product/

# @param {Integer} n
# @return {String}
def smallest_number(n)
  return "0" if n == 0
  return "1" if n == 1

  digits = []
  9.downto(2) do |d|
    while n % d == 0
      digits << d.to_s
      n /= d
    end
  end
  return "-1" if n > 1

  digits.reverse.join
end
