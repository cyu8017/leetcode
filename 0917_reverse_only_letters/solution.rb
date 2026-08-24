# LeetCode 0917 - Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/

# @param {String} s
# @return {String}
def reverse_only_letters(s)
  chars = s.chars
  i = 0
  j = chars.length - 1
  while i < j
    i += 1 while i < j && chars[i] !~ /[A-Za-z]/
    j -= 1 while i < j && chars[j] !~ /[A-Za-z]/
    chars[i], chars[j] = chars[j], chars[i]
    i += 1
    j -= 1
  end
  chars.join
end
