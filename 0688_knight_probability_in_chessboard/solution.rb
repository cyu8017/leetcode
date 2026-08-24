# LeetCode 0688 - Knight Probability in Chessboard
# https://leetcode.com/problems/knight-probability-in-chessboard/

# @param {Integer} n
# @param {Integer} k
# @param {Integer} row
# @param {Integer} column
# @return {Float}
def knight_probability(n, k, row, column)
  moves = [
    [-2, -1], [-2, 1], [-1, -2], [-1, 2],
    [1, -2], [1, 2], [2, -1], [2, 1]
  ]
  dp = Array.new(n) { Array.new(n, 0.0) }
  dp[row][column] = 1.0

  k.times do
    nxt = Array.new(n) { Array.new(n, 0.0) }
    n.times do |r|
      n.times do |c|
        next if dp[r][c] == 0

        moves.each do |dr, dc|
          nr = r + dr
          nc = c + dc
          nxt[nr][nc] += dp[r][c] / 8.0 if nr >= 0 && nr < n && nc >= 0 && nc < n
        end
      end
    end
    dp = nxt
  end

  dp.sum { |r| r.sum }
end
