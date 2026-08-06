# LeetCode 1138 - Alphabet Board Path
# https://leetcode.com/problems/alphabet-board-path/

# @param {String} target
# @return {String}
def alphabet_board_path(target)
  row = 0
  col = 0
  ans = []
  target.each_char do |ch|
    r = (ch.ord - "a".ord) / 5
    c = (ch.ord - "a".ord) % 5
    # Move U/L before D/R to avoid falling off 'z'
    while row > r
      ans << "U"
      row -= 1
    end
    while col > c
      ans << "L"
      col -= 1
    end
    while row < r
      ans << "D"
      row += 1
    end
    while col < c
      ans << "R"
      col += 1
    end
    ans << "!"
  end
  ans.join
end
