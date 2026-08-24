# LeetCode 0738 - Monotone Increasing Digits
# https://leetcode.com/problems/monotone-increasing-digits/

# @param {Integer} n
# @return {Integer}
def monotone_increasing_digits(n)
  digits = n.to_s.chars
  mark = digits.length
  (digits.length - 1).downto(1) do |i|
    if digits[i] < digits[i - 1]
      digits[i - 1] = (digits[i - 1].to_i - 1).to_s
      mark = i
    end
  end
  (mark...digits.length).each { |i| digits[i] = "9" }
  digits.join.to_i
end
