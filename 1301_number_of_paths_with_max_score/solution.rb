# LeetCode 1301 - Number Of Paths With Max Score
# https://leetcode.com/problems/number-of-paths-with-max-score/

def paths_with_max_score(board)
  mod = 1_000_000_007
  n = board.length
  score = Array.new(n) { Array.new(n, -1) }
  ways = Array.new(n) { Array.new(n, 0) }
  score[n - 1][n - 1] = 0
  ways[n - 1][n - 1] = 1
  (n - 1).downto(0) do |r|
    (n - 1).downto(0) do |c|
      next if board[r][c] == 'X' || (r == n - 1 && c == n - 1)
      best = -1
      count = 0
      [[r + 1, c], [r, c + 1], [r + 1, c + 1]].each do |nr, nc|
        next unless nr < n && nc < n && score[nr][nc] >= 0
        if score[nr][nc] > best
          best = score[nr][nc]
          count = ways[nr][nc]
        elsif score[nr][nc] == best
          count = (count + ways[nr][nc]) % mod
        end
      end
      if best >= 0
        add = board[r][c] =~ /\d/ ? board[r][c].to_i : 0
        score[r][c] = best + add
        ways[r][c] = count
      end
    end
  end
  [[score[0][0], 0].max, ways[0][0]]
end
