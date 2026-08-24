# LeetCode 3146 - Permutation Difference between Two Strings
# https://leetcode.com/problems/permutation-difference-between-two-strings/

# @param {String} s
# @param {String} t
# @return {Integer}
def find_permutation_difference(s, t)
  d = Array.new(26, 0)
  s.each_char.with_index { |ch, i| d[ch.ord - 97] = i }
  ans = 0
  t.each_char.with_index { |ch, i| ans += (d[ch.ord - 97] - i).abs }
  ans
end
