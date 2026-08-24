# LeetCode 0902 - Numbers At Most N Given Digit Set
# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

# @param {String[]} digits
# @param {Integer} n
# @return {Integer}
def at_most_n_given_digit_set(digits, n)
  s = n.to_s
  m = s.length
  digits = digits.sort
  k = digits.length

  count_len = ->(length) { k**length }
  count_up_to = lambda do |str|
    return 0 if str.empty?

    first = digits.count { |d| d < str[0] }
    ways = first * (k**(str.length - 1))
    ways += count_up_to.call(str[1..]) if digits.include?(str[0])
    ways
  end

  ans = (1...m).sum { |i| count_len.call(i) }
  ans + count_up_to.call(s)
end
