# LeetCode 0542 - 01 Matrix
# https://leetcode.com/problems/01-matrix/

class Solution
  def update_matrix(mat)
    rows = mat.length
    cols = mat[0].length
    dist = Array.new(rows) { Array.new(cols, 1_000_000_000) }
    queue = []

    (0...rows).each do |row|
      (0...cols).each do |col|
        if mat[row][col].zero?
          dist[row][col] = 0
          queue << [row, col]
        end
      end
    end

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    until queue.empty?
      row, col = queue.shift
      directions.each do |dr, dc|
        nr = row + dr
        nc = col + dc
        next unless nr.between?(0, rows - 1) && nc.between?(0, cols - 1)

        candidate = dist[row][col] + 1
        if dist[nr][nc] > candidate
          dist[nr][nc] = candidate
          queue << [nr, nc]
        end
      end
    end

    dist
  end

  alias_method :updateMatrix, :update_matrix
end
