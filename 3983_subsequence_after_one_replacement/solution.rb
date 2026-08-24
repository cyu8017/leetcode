# LeetCode 3983 - Subsequence After One Replacement
# https://leetcode.com/problems/subsequence-after-one-replacement/

# @param {String} s
# @param {String} t
# @return {Boolean}
def can_make_subsequence(s, t)
  m = s.length
  n = t.length
  i0 = 0
  i1 = 0
  j = 0
  while i1 < m && j < n
    i1 += 1 if s[i1] == t[j]
    i1 = i0 + 1 if i1 < i0 + 1
    i0 += 1 if s[i0] == t[j]
    j += 1
  end
  i1 == m
end
