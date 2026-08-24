# LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

# @param {String} str1
# @param {String} str2
# @return {Boolean}
def can_make_subsequence(str1, str2)
  j = 0
  i = 0
  while i < str1.length && j < str2.length
    a = str1[i].ord - 97
    b = str2[j].ord - 97
    j += 1 if a == b || (a + 1) % 26 == b
    i += 1
  end
  j == str2.length
end
