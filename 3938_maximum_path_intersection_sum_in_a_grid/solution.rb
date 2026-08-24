# LeetCode 3938 - Maximum Path Intersection Sum in a Grid
# https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def max_path_sum(grid)
  check_line = lambda do |length, value|
    answer = -2_147_483_648
    best_ending = value.call(0) + value.call(1)
    answer = best_ending if best_ending > answer
    (2...length).each do |i|
      if value.call(i - 1) + value.call(i) > best_ending + value.call(i)
        best_ending = value.call(i - 1) + value.call(i)
      else
        best_ending += value.call(i)
      end
      answer = best_ending if best_ending > answer
    end
    answer
  end
  rows = grid.length
  cols = grid[0].length
  answer = -2_147_483_648
  rows.times do |row|
    r = row
    v = check_line.call(cols, ->(col) { grid[r][col] })
    answer = v if v > answer
  end
  cols.times do |col|
    c = col
    v = check_line.call(rows, ->(row) { grid[row][c] })
    answer = v if v > answer
  end
  (1...(rows - 1)).each do |row|
    (1...(cols - 1)).each do |col|
      answer = grid[row][col] if grid[row][col] > answer
    end
  end
  answer
end
