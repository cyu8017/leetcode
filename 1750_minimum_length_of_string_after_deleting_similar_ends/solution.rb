# LeetCode 1750 - Minimum Length of String After Deleting Similar Ends
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

# @param {String} s
# @return {Integer}
def minimum_length(s)
  left = 0
  right = s.length - 1
  while left < right && s[left] == s[right]
    ch = s[left]
    left += 1 while left <= right && s[left] == ch
    right -= 1 while left <= right && s[right] == ch
  end
  right - left + 1
end
