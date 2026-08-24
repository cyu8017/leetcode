# LeetCode 3740 - Minimum Distance Between Three Equal Elements I
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

# @param {Integer[]} nums
# @return {Integer}
def minimum_distance(nums)
  g = Hash.new { |h, k| h[k] = [] }
  nums.each_with_index { |x, i| g[x] << i }
  inf = 1 << 30
  ans = inf
  g.each_value do |ls|
    m = ls.length
    (0...(m - 2)).each { |h| ans = [ans, (ls[h + 2] - ls[h]) * 2].min }
  end
  ans == inf ? -1 : ans
end
