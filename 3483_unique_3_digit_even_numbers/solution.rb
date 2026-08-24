# LeetCode 3483 - Unique 3-Digit Even Numbers
# https://leetcode.com/problems/unique-3-digit-even-numbers/

# @param {Integer[]} digits
# @return {Integer}
def total_numbers(digits)
  seen = {}
  n = digits.length
  (0...n).each do |i|
    (0...n).each do |j|
      next if j == i

      (0...n).each do |k|
        next if k == i || k == j
        next if digits[i] == 0
        next if digits[k].odd?

        seen[digits[i] * 100 + digits[j] * 10 + digits[k]] = true
      end
    end
  end
  seen.length
end
