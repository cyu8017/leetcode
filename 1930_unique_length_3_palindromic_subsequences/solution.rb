# LeetCode 1930 - Unique Length-3 Palindromic Subsequences
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

# @param {String} s
# @return {Integer}
def count_palindromic_subsequence(s)
  first = {}
  last = {}
  s.chars.each_with_index do |c, i|
    first[c] = i unless first.key?(c)
    last[c] = i
  end
  ans = 0
  first.each do |c, f|
    l = last[c]
    ans += s[(f + 1)...l].chars.uniq.length if l - f > 1
  end
  ans
end
