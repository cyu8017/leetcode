# LeetCode 2486 - Append Characters to String to Make Subsequence
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

# @param {String} s
# @param {String} t
# @return {Integer}
def append_characters(s, t)
  j = 0
  i = 0
  while i < s.length && j < t.length
    j += 1 if s[i] == t[j]
    i += 1
  end
  t.length - j
end
