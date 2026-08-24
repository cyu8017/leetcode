# LeetCode 3693 - Climbing Stairs II
# https://leetcode.com/problems/climbing-stairs-ii/

# @param {Integer} n
# @param {Integer[]} costs
# @return {Integer}
def climb_stairs(n, costs)
  inf = 10**9
  f = Array.new(n + 1, inf)
  f[0] = 0
  (1..n).each do |i|
    x = costs[i - 1]
    ([0, i - 3].max...i).each do |j|
      v = f[j] + x + (i - j) * (i - j)
      f[i] = v if v < f[i]
    end
  end
  f[n]
end
