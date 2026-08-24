# LeetCode 2259 - Remove Digit From Number to Maximize Result
# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

# @param {String} number
# @param {String} digit
# @return {String}
def remove_digit(number, digit)
  best = ""
  number.chars.each_with_index do |ch, i|
    next unless ch == digit

    cand = number[0...i] + number[(i + 1)..]
    best = cand if cand > best
  end
  best
end
