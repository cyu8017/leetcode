# LeetCode 3136 - Valid Word
# https://leetcode.com/problems/valid-word/

# @param {String} word
# @return {Boolean}
def is_valid(word)
  return false if word.length < 3
  has_vowel = false
  has_consonant = false
  vs = Array.new(26, false)
  "aeiou".each_char { |c| vs[c.ord - 97] = true }
  word.each_char do |c|
    if c =~ /[A-Za-z]/
      lower = c.downcase
      if vs[lower.ord - 97]
        has_vowel = true
      else
        has_consonant = true
      end
    elsif c !~ /\d/
      return false
    end
  end
  has_vowel && has_consonant
end
