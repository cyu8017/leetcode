# LeetCode 3933 - Largest Local Values in a Matrix II
# https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

# @param {Integer[][]} matrix
# @return {Integer}
def count_local_maximums(matrix)
  rows = matrix.length
  cols = matrix[0].length
  positions = Array.new(201) { [] }
  rows.times do |row|
    cols.times do |col|
      value = matrix[row][col]
      positions[value] << [row, col] if value > 0
    end
  end
  answer = 0
  (1..200).each do |value|
    next if positions[value].empty?
    prefix = Array.new(rows + 1) { Array.new(cols + 1, 0) }
    rows.times do |row|
      cols.times do |col|
        add = matrix[row][col] > value ? 1 : 0
        prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add
      end
    end
    positions[value].each do |row, col|
      top = [0, row - value].max
      bottom = [rows - 1, row + value].min
      left = [0, col - value].max
      right = [cols - 1, col + value].min
      greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left]
      [-value, value].each do |dr|
        [-value, value].each do |dc|
          rr = row + dr
          cc = col + dc
          greater -= 1 if rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix[rr][cc] > value
        end
      end
      answer += 1 if greater == 0
    end
  end
  answer
end
