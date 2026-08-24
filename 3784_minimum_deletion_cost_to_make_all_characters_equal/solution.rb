# LeetCode 3784 - Minimum Deletion Cost to Make All Characters Equal
# https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

# @param {String} s
# @param {Integer[]} cost
# @return {Integer}
def min_cost(s, cost)
  tot = 0
  g = Hash.new(0)
  (0...cost.length).each do |i|
    tot += cost[i]
    g[s[i]] += cost[i]
  end
  ans = tot
  g.each_value { |x| ans = [ans, tot - x].min }
  ans
end
