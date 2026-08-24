# LeetCode 2586 - Count the Number of Vowel Strings in Range
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

# @param {String[]} words
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def vowel_strings(words, left, right)
  is_v = lambda { |c| c == "a" || c == "e" || c == "i" || c == "o" || c == "u" }
  ans = 0
  (left..right).each do |i|
    w = words[i]
    ans += 1 if is_v.call(w[0]) && is_v.call(w[-1])
  end
  ans
end
