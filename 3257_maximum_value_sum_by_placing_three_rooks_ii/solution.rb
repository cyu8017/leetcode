# LeetCode 3257 - Maximum Value Sum by Placing Three Rooks II
# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/

# @param {Integer[][]} board
# @return {Integer}
def maximum_value_sum(board)
  m = board.length
  n = board[0].length
  tops = []
  (0...m).each do |i|
    row = []
    (0...n).each do |j|
      cur = { v: board[i][j], c: j }
      placed = false
      row.each_index do |t|
        if cur[:v] > row[t][:v]
          row.insert(t, cur)
          placed = true
          break
        end
      end
      row << cur unless placed
      row = row[0, 3] if row.length > 3
    end
    tops << row
  end
  ans = -(10**18)
  (0...m).each do |i|
    tops[i].each do |a|
      ((i + 1)...m).each do |j|
        tops[j].each do |b|
          next if a[:c] == b[:c]
          ((j + 1)...m).each do |k|
            tops[k].each do |c|
              next if c[:c] == a[:c] || c[:c] == b[:c]
              s = a[:v] + b[:v] + c[:v]
              ans = s if s > ans
            end
          end
        end
      end
    end
  end
  ans
end
