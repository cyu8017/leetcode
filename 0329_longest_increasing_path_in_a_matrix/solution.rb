# LeetCode 0329 - Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution
  def longestIncreasingPath(matrix)
    return 0 if matrix.empty? || matrix[0].empty?

    rows = matrix.length
    cols = matrix[0].length
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    memo = {}

    dfs = lambda do |row, col|
      key = row * cols + col
      return memo[key] if memo.key?(key)

      best = 1
      directions.each do |dr, dc|
        nr = row + dr
        nc = col + dc
        next unless nr.between?(0, rows - 1) && nc.between?(0, cols - 1)
        next unless matrix[nr][nc] > matrix[row][col]

        best = [best, 1 + dfs.call(nr, nc)].max
      end
      memo[key] = best
    end

    (0...rows).flat_map { |row| (0...cols).map { |col| dfs.call(row, col) } }.max
  end
end
