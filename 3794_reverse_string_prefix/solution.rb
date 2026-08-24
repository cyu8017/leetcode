# LeetCode 3794 - Reverse String Prefix
# https://leetcode.com/problems/reverse-string-prefix/

# @param {String} s
# @param {Integer} k
# @return {String}
def reverse_prefix(s, k)
  arr = s.chars
  i = 0
  j = k - 1
  while i < j
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
  end
  arr.join
end
