# LeetCode 3800 - Minimum Cost to Make Two Binary Strings Equal
# https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

# @param {String} s
# @param {String} t
# @param {Integer} flip_cost
# @param {Integer} swap_cost
# @param {Integer} cross_cost
# @return {Integer}
def minimum_cost(s, t, flip_cost, swap_cost, cross_cost)
  diff = [0, 0]
  n = s.length
  (0...n).each { |i| diff[s[i].ord - 48] += 1 if s[i] != t[i] }
  ans = (diff[0] + diff[1]) * flip_cost
  mx = [diff[0], diff[1]].max
  mn = [diff[0], diff[1]].min
  ans = [ans, mn * swap_cost + (mx - mn) * flip_cost].min
  avg = (mx + mn) / 2
  ans = [ans, (avg - mn) * cross_cost + avg * swap_cost + (mx + mn - avg * 2) * flip_cost].min
  ans
end
