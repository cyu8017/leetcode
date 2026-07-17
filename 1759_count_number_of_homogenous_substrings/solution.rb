# LeetCode 1759 - Count Number of Homogenous Substrings
# https://leetcode.com/problems/count-number-of-homogenous-substrings/

# @param {String} s
# @return {Integer}
def count_homogenous(s)
  mod = 1_000_000_007
  ans = 0
  i = 0
  while i < s.length
    j = i
    j += 1 while j < s.length && s[j] == s[i]
    length = j - i
    ans = (ans + length * (length + 1) / 2) % mod
    i = j
  end
  ans
end
