# LeetCode 1163 - Last Substring in Lexicographical Order
# https://leetcode.com/problems/last-substring-in-lexicographical-order/

# @param {String} s
# @return {String}
def last_substring(s)
  i = 0
  j = 1
  k = 0
  n = s.length
  while j + k < n
    if s[i + k] == s[j + k]
      k += 1
      next
    end
    if s[i + k] > s[j + k]
      j = j + k + 1
    else
      i = [i + k + 1, j].max
      j = i + 1
    end
    k = 0
  end
  s[i..]
end
