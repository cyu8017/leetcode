# LeetCode 2063 - Vowels of All Substrings
# https://leetcode.com/problems/vowels-of-all-substrings/

# @param {String} word
# @return {Integer}
def count_vowels(word)
  vowels = { "a" => true, "e" => true, "i" => true, "o" => true, "u" => true }
  n = word.length
  ans = 0
  word.each_char.with_index do |c, i|
    ans += (i + 1) * (n - i) if vowels[c]
  end
  ans
end
