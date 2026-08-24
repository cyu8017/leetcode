# LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

# @param {String} word1
# @param {String} word2
# @return {Integer}
def valid_substring_count(word1, word2)
  need = Array.new(26, 0)
  required = 0
  word2.each_char do |c|
    i = c.ord - 97
    required += 1 if need[i] == 0
    need[i] += 1
  end
  have = Array.new(26, 0)
  formed = 0
  ans = 0
  l = 0
  word1.length.times do |r|
    c = word1[r].ord - 97
    have[c] += 1
    formed += 1 if have[c] == need[c] && need[c] > 0
    while formed == required && l <= r
      ans += word1.length - r
      c2 = word1[l].ord - 97
      formed -= 1 if have[c2] == need[c2] && need[c2] > 0
      have[c2] -= 1
      l += 1
    end
  end
  ans
end
