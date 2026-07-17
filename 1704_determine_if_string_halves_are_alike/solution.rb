# LeetCode 1704 - Determine if String Halves Are Alike
# https://leetcode.com/problems/determine-if-string-halves-are-alike/

# @param {String} s
# @return {Boolean}
def halves_are_alike(s)
  mid = s.length / 2
  s[0...mid].count("aeiouAEIOU") == s[mid..].count("aeiouAEIOU")
end
