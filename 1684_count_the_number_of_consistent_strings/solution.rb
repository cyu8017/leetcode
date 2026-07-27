# LeetCode 1684 - Count the Number of Consistent Strings
# https://leetcode.com/problems/count-the-number-of-consistent-strings/

# @param {String} allowed
# @param {String[]} words
# @return {Integer}
def count_consistent_strings(allowed, words)
  a = allowed.chars.to_h { |c| [c, true] }
  words.count { |w| w.chars.all? { |c| a[c] } }
end
