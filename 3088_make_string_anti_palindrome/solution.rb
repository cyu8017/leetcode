# LeetCode 3088 - Make String Anti-palindrome
# https://leetcode.com/problems/make-string-anti-palindrome/

# @param {String} s
# @return {String}
def make_anti_palindrome(s)
  arr = s.chars.sort
  n = arr.length
  m = n / 2
  if arr[m] == arr[m - 1]
    i = m
    i += 1 while i < n && arr[i] == arr[i - 1]
    j = m
    while j < n && arr[j] == arr[n - j - 1]
      return "-1" if i >= n
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j += 1
    end
  end
  arr.join
end
