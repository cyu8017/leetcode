# LeetCode 1937 - Maximum Number of Points with Cost
# https://leetcode.com/problems/maximum-number-of-points-with-cost/

# @param {Integer[][]} points
# @return {Integer}
def max_points(points)
  m = points.length
  n = points[0].length
  prev = points[0].dup
  (1...m).each do |r|
    left = Array.new(n)
    right = Array.new(n)
    cur = Array.new(n)
    left[0] = prev[0]
    (1...n).each { |c| left[c] = [left[c - 1] - 1, prev[c]].max }
    right[n - 1] = prev[n - 1]
    (n - 2).downto(0) { |c| right[c] = [right[c + 1] - 1, prev[c]].max }
    n.times { |c| cur[c] = points[r][c] + [left[c], right[c]].max }
    prev = cur
  end
  prev.max
end
