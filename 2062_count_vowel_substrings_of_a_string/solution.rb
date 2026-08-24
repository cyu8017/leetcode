# LeetCode 2062 - Count Vowel Substrings of a String
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/

# @param {String} word
# @return {Integer}
def count_vowel_substrings(word)
  vowels = { "a" => true, "e" => true, "i" => true, "o" => true, "u" => true }
  ans = 0
  n = word.length
  n.times do |i|
    seen = {}
    (i...n).each do |j|
      break unless vowels[word[j]]

      seen[word[j]] = true
      ans += 1 if seen.length == 5
    end
  end
  ans
end
