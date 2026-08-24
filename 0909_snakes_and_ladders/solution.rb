# LeetCode 0909 - Snakes and Ladders
# https://leetcode.com/problems/snakes-and-ladders/

# @param {Integer[][]} board
# @return {Integer}
def snakes_and_ladders(board)
  n = board.length

  pos = lambda do |square|
    square -= 1
    row = square / n
    rem = square % n
    r = n - 1 - row
    c = row.even? ? rem : n - 1 - rem
    [r, c]
  end

  target = n * n
  queue = [1]
  seen = { 1 => true }
  moves = 0
  until queue.empty?
    queue.length.times do
      cur = queue.shift
      return moves if cur == target

      ((cur + 1)..[cur + 6, target].min).each do |nxt|
        r, c = pos.call(nxt)
        nxt = board[r][c] if board[r][c] != -1
        unless seen[nxt]
          seen[nxt] = true
          queue << nxt
        end
      end
    end
    moves += 1
  end
  -1
end
