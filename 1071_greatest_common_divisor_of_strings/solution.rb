# LeetCode 1071 - Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/

# @param {String} str1
# @param {String} str2
# @return {String}
def gcd_of_strings(str1, str2)
  return "" if str1 + str2 != str2 + str1

  a = str1.length
  b = str2.length
  while b != 0
    a, b = b, a % b
  end
  str1[0, a]
end
