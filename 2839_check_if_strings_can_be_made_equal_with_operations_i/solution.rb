# LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

# @param {String} s1
# @param {String} s2
# @return {Boolean}
def can_be_equal(s1, s2)
  a = [s1[0], s1[2]].sort.join
  b = [s2[0], s2[2]].sort.join
  c = [s1[1], s1[3]].sort.join
  d = [s2[1], s2[3]].sort.join
  a == b && c == d
end
