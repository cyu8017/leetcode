# LeetCode 0576 - Out of Boundary Paths
# https://leetcode.com/problems/out-of-boundary-paths/

# @param {Integer} m
# @param {Integer} n
# @param {Integer} max_move
# @param {Integer} start_row
# @param {Integer} start_column
# @return {Integer}
def find_paths(m, n, max_move, start_row, start_column)
  mod = 10**9 + 7
  dp = Array.new(m) { Array.new(n, 0) }
  dp[start_row][start_column] = 1
  result = 0
  directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

  max_move.times do
    nxt = Array.new(m) { Array.new(n, 0) }
    m.times do |row|
      n.times do |col|
        ways = dp[row][col]
        next if ways.zero?

        directions.each do |dr, dc|
          nr = row + dr
          nc = col + dc
          if nr >= 0 && nr < m && nc >= 0 && nc < n
            nxt[nr][nc] = (nxt[nr][nc] + ways) % mod
          else
            result = (result + ways) % mod
          end
        end
      end
    end
    dp = nxt
  end

  result
end
