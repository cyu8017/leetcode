# LeetCode 3460 - Longest Common Prefix After at Most One Removal
# https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

# @param {String} s
# @param {String} t
# @return {Integer}
def longest_common_prefix(s, t)
  i = 0
  j = 0
  removed = false
  while i < s.length && j < t.length
    if s[i] == t[j]
      i += 1
      j += 1
      next
    end
    break if removed

    removed = true
    i += 1
  end
  j
end
