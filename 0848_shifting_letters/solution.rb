# LeetCode 0848 - Shifting Letters
# https://leetcode.com/problems/shifting-letters/

# @param {String} s
# @param {Integer[]} shifts
# @return {String}
def shifting_letters(s, shifts)
  total = 0
  chars = s.chars
  (s.length - 1).downto(0) do |i|
    total = (total + shifts[i]) % 26
    chars[i] = ((chars[i].ord - 97 + total) % 26 + 97).chr
  end
  chars.join
end
