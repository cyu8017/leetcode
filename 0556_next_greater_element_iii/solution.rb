# LeetCode 0556 - Next Greater Element III
# https://leetcode.com/problems/next-greater-element-iii/

# @param {Integer} n
# @return {Integer}
def next_greater_element(n)
  digits = n.to_s.chars
  i = digits.length - 2
  i -= 1 while i >= 0 && digits[i] >= digits[i + 1]
  return -1 if i < 0

  j = digits.length - 1
  j -= 1 while digits[j] <= digits[i]
  digits[i], digits[j] = digits[j], digits[i]
  digits[(i + 1)..] = digits[(i + 1)..].reverse

  value = digits.join.to_i
  value <= 2**31 - 1 ? value : -1
end
