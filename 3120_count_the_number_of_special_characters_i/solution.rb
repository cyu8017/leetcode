# LeetCode 3120 - Count the Number of Special Characters I
# https://leetcode.com/problems/count-the-number-of-special-characters-i/

# @param {String} word
# @return {Integer}
def number_of_special_chars(word)
  s = Array.new(128, false)
  word.each_char { |ch| s[ch.ord] = true }
  ans = 0
  26.times { |i| ans += 1 if s[97 + i] && s[65 + i] }
  ans
end
