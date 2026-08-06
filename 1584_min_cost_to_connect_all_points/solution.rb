# LeetCode 1584 - Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/

# @param {Integer[][]} points
# @return {Integer}
def min_cost_connect_points(points)
  n = points.length
  used = Array.new(n, false)
  dist = Array.new(n, 10**9)
  dist[0] = 0
  answer = 0
  n.times do
    u = (0...n).reject { |i| used[i] }.min_by { |i| dist[i] }
    used[u] = true
    answer += dist[u]
    (0...n).each do |v|
      next if used[v]
      d = (points[u][0] - points[v][0]).abs + (points[u][1] - points[v][1]).abs
      dist[v] = d if d < dist[v]
    end
  end
  answer
end
