# LeetCode 3844 - Longest Almost-Palindromic Substring
# https://leetcode.com/problems/longest-almost-palindromic-substring/

# @param {String} s
# @return {Integer}
def almost_palindromic(s)
  n = s.length
  ans = 0
  (0...n).each do |i|
    ans = [ans, [expand_3844(s, i, i), expand_3844(s, i, i + 1)].max].max
  end
  ans
end

def expand_3844(s, l, r)
  n = s.length
  while l >= 0 && r < n && s[l] == s[r]
    l -= 1
    r += 1
  end
  l1 = l - 1
  r1 = r
  l2 = l
  r2 = r + 1
  while l1 >= 0 && r1 < n && s[l1] == s[r1]
    l1 -= 1
    r1 += 1
  end
  while l2 >= 0 && r2 < n && s[l2] == s[r2]
    l2 -= 1
    r2 += 1
  end
  [n, [r1 - l1 - 1, r2 - l2 - 1].max].min
end
