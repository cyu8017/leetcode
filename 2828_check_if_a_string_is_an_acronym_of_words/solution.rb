# LeetCode 2828 - Check if a String Is an Acronym of Words
# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

# @param {String[]} words
# @param {String} s
# @return {Boolean}
def is_acronym(words, s)
  return false if words.length != s.length
  words.each_with_index do |w, i|
    return false if w.nil? || w.empty? || w[0] != s[i]
  end
  true
end
