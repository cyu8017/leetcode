# LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
# https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

# @param {Integer[][]} board
# @param {String[]} pattern
# @return {Integer[]}
def find_pattern(board, pattern)
  m = board.length
  n = board[0].length
  r = pattern.length
  c = pattern[0].length

  check = lambda do |i, j|
    d1 = Array.new(26, 0)
    d2 = Array.new(10, 0)
    r.times do |a|
      c.times do |b|
        x = i + a
        y = j + b
        ch = pattern[a][b]
        if ch >= "0" && ch <= "9"
          return false if ch.ord - 48 != board[x][y]
        else
          v = ch.ord - 97
          return false if d1[v] > 0 && d1[v] - 1 != board[x][y]
          return false if d2[board[x][y]] > 0 && d2[board[x][y]] - 1 != v
          d1[v] = board[x][y] + 1
          d2[board[x][y]] = v + 1
        end
      end
    end
    true
  end

  (0..m - r).each do |i|
    (0..n - c).each do |j|
      return [i, j] if check.call(i, j)
    end
  end
  [-1, -1]
end
