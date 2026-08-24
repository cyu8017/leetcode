# LeetCode 2078 - Two Furthest Houses With Different Colors
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

# @param {Integer[]} colors
# @return {Integer}
def max_distance(colors)
  n = colors.length
  ans = 0
  colors.each_with_index do |c, i|
    ans = [ans, i].max if c != colors[0]
    ans = [ans, n - 1 - i].max if c != colors[n - 1]
  end
  ans
end
