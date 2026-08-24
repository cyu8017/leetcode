# LeetCode 3813 - Vowel Consonant Score
# https://leetcode.com/problems/vowel-consonant-score/

# @param {String} s
# @return {Integer}
def vowel_consonant_score(s)
  v = 0
  c = 0
  s.each_char do |ch|
    if (ch >= "a" && ch <= "z") || (ch >= "A" && ch <= "Z")
      c += 1
      v += 1 if "aeiou".include?(ch)
    end
  end
  c -= v
  return 0 if c == 0
  v / c
end
