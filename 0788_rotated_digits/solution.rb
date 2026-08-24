# LeetCode 0788 - Rotated Digits
# https://leetcode.com/problems/rotated-digits/

# @param {Integer} n
# @return {Integer}
def rotated_digits(n)
  valid = %w[0 1 2 5 6 8 9]
  changing = %w[2 5 6 9]
  count = 0
  (1..n).each do |num|
    s = num.to_s.chars
    count += 1 if s.all? { |ch| valid.include?(ch) } && s.any? { |ch| changing.include?(ch) }
  end
  count
end
