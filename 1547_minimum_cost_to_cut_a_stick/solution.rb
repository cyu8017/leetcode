# LeetCode 1547 - Minimum Cost to Cut a Stick
# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

# @param {Integer} n
# @param {Integer[]} cuts
# @return {Integer}
def min_cost(n, cuts)
  points = [0] + cuts.sort + [n]
  size = points.length
  dp = Array.new(size) { Array.new(size, 0) }
  (2...size).each do |width|
    (0...(size - width)).each do |left|
      right = left + width
      best = Float::INFINITY
      ((left + 1)...right).each do |mid|
        best = [best, dp[left][mid] + dp[mid][right]].min
      end
      best = 0 if best == Float::INFINITY
      dp[left][right] = best
      dp[left][right] += points[right] - points[left] if right > left + 1
    end
  end
  dp[0][-1]
end
