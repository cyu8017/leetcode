# LeetCode 2285 - Maximum Total Importance of Roads
# https://leetcode.com/problems/maximum-total-importance-of-roads/

# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def maximum_importance(n, roads)
  deg = Array.new(n, 0)
  roads.each do |a, b|
    deg[a] += 1
    deg[b] += 1
  end
  deg.sort!
  ans = 0
  n.times { |i| ans += deg[i] * (i + 1) }
  ans
end
