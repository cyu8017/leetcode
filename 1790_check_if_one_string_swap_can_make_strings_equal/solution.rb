# LeetCode 1790 - Check if One String Swap Can Make Strings Equal
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

# @param {String} s1
# @param {String} s2
# @return {Boolean}
def are_almost_equal(s1, s2)
  diff = (0...s1.length).select { |i| s1[i] != s2[i] }
  return true if diff.empty?
  diff.length == 2 && s1[diff[0]] == s2[diff[1]] && s1[diff[1]] == s2[diff[0]]
end
