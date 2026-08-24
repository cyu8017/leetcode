# LeetCode 3888 - Minimum Operations to Make All Grid Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def min_operations(grid, k)
  m = grid.length
  n = grid[0].length
  max_val = grid[0][0]
  grid.each { |row| row.each { |x| max_val = [max_val, x].max } }
  check = lambda do |target|
    diff = Array.new(m + 2) { Array.new(n + 2, 0) }
    total_ops = 0
    (1..m).each do |i|
      (1..n).each do |j|
        diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        cur_val = grid[i - 1][j - 1] + diff[i][j]
        return -1 if cur_val > target
        if cur_val < target
          return -1 if i + k - 1 > m || j + k - 1 > n
          needed = target - cur_val
          total_ops += needed
          diff[i][j] += needed
          diff[i + k][j] -= needed
          diff[i][j + k] -= needed
          diff[i + k][j + k] += needed
        end
      end
    end
    total_ops
  end
  (max_val..(max_val + 1)).each do |t|
    res = check.call(t)
    return res if res != -1
  end
  -1
end
