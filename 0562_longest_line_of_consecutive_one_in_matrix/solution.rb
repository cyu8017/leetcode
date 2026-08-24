# LeetCode 0562 - Longest Line of Consecutive One in Matrix
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

# @param {Integer[][]} mat
# @return {Integer}
def longest_line(mat)
  return 0 if mat.nil? || mat.empty? || mat[0].empty?

  rows = mat.length
  cols = mat[0].length
  dp = Array.new(rows) { Array.new(cols) { [0, 0, 0, 0] } }
  best = 0

  rows.times do |r|
    cols.times do |c|
      next if mat[r][c].zero?

      dp[r][c][0] = (c > 0 ? dp[r][c - 1][0] : 0) + 1
      dp[r][c][1] = (r > 0 ? dp[r - 1][c][1] : 0) + 1
      dp[r][c][2] = (r > 0 && c > 0 ? dp[r - 1][c - 1][2] : 0) + 1
      dp[r][c][3] = (r > 0 && c + 1 < cols ? dp[r - 1][c + 1][3] : 0) + 1
      best = [best, dp[r][c].max].max
    end
  end

  best
end
