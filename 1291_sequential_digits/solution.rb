# LeetCode 1291 - Sequential Digits
# https://leetcode.com/problems/sequential-digits/

# @param {Integer} low
# @param {Integer} high
# @return {Integer[]}
def sequential_digits(low, high)
  digits = "123456789"
  answer = []
  (2..9).each do |length|
    (0..(9 - length)).each do |start|
      value = digits[start, length].to_i
      answer << value if value.between?(low, high)
    end
  end
  answer
end
