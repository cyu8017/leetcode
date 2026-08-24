# LeetCode 2937 - Make Three Strings Equal
# https://leetcode.com/problems/make-three-strings-equal/

# @param {String} s1
# @param {String} s2
# @param {String} s3
# @return {Integer}
def find_minimum_operations(s1, s2, s3)
  n = [s1.length, s2.length, s3.length].min
  i = 0
  while i < n && s1[i] == s2[i] && s2[i] == s3[i]
    i += 1
  end
  return -1 if i == 0

  s1.length + s2.length + s3.length - 3 * i
end
