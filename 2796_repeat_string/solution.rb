# LeetCode 2796 - Repeat String
# https://leetcode.com/problems/repeat-string/

# @param {String} s
# @param {Integer} times
# @return {String}
def replicate(s, times)
  res = +""
  times.times { res << s }
  res
end
