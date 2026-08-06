# LeetCode 1933 - Check if String Is Decomposable Into Value-Equal Substrings
# https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

# @param {String} s
# @return {Boolean}
def is_decomposable(s)
  n = s.length
  i = 0
  twos = 0
  while i < n
    j = i
    j += 1 while j < n && s[j] == s[i]
    length = j - i
    return false if length % 3 == 1
    if length % 3 == 2
      twos += 1
      return false if twos > 1
    end
    i = j
  end
  twos == 1
end
