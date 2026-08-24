# LeetCode 3796 - Find Maximum Value in a Constrained Sequence
# https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

# @param {Integer} n
# @param {Integer[][]} restrictions
# @param {Integer[]} diff
# @return {Integer}
def max_value(n, restrictions, diff)
  inf = 2147483647 / 4
  bound = Array.new(n, inf)
  bound[0] = 0
  restrictions.each { |r| bound[r[0]] = r[1] }
  (1...n).each { |i| bound[i] = [bound[i], bound[i - 1] + diff[i - 1]].min }
  (n - 2).downto(0) { |i| bound[i] = [bound[i], bound[i + 1] + diff[i]].min }
  ans = bound[0]
  (1...n).each { |i| ans = [ans, bound[i]].max }
  ans
end
