# LeetCode 2712 - Minimum Cost to Make All Characters Equal
# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

# @param {String} s
# @return {Integer}
def minimum_cost(s)
  n = s.length
  ans = 0
  (1...n).each { |i| ans += [i, n - i].min if s[i] != s[i - 1] }
  ans
end
