# LeetCode 2018 - Check if Word Can Be Placed In Crossword
# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

# @param {Character[][]} board
# @param {String} word
# @return {Boolean}
def place_word_in_crossword(board, word)
  m = board.length
  n = board[0].length
  len = word.length

  match = lambda do |cells|
    return false if cells.length != len

    ok1 = ok2 = true
    len.times do |i|
      ok1 = false if cells[i] != " " && cells[i] != word[i]
      ok2 = false if cells[i] != " " && cells[i] != word[len - 1 - i]
    end
    ok1 || ok2
  end

  m.times do |r|
    c = 0
    while c < n
      c += 1 while c < n && board[r][c] == "#"
      start = c
      c += 1 while c < n && board[r][c] != "#"
      if c - start == len
        sb = (start...c).map { |i| board[r][i] }.join
        return true if match.call(sb)
      end
    end
  end
  n.times do |c|
    r = 0
    while r < m
      r += 1 while r < m && board[r][c] == "#"
      start = r
      r += 1 while r < m && board[r][c] != "#"
      if r - start == len
        sb = (0...len).map { |i| board[start + i][c] }.join
        return true if match.call(sb)
      end
    end
  end
  false
end
