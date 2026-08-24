# LeetCode 3546 - Equal Sum Grid Partition I
# https://leetcode.com/problems/equal-sum-grid-partition-i/

# @param {Integer[][]} grid
# @return {Boolean}
def can_partition_grid(grid)
  s = 0
  grid.each { |row| row.each { |x| s += x } }
  return false if s.odd?
  m = grid.length
  n = grid[0].length
  pre = 0
  (0...m).each do |i|
    grid[i].each { |x| pre += x }
    return true if pre * 2 == s && i + 1 < m
  end
  pre = 0
  (0...n).each do |j|
    (0...m).each { |i| pre += grid[i][j] }
    return true if pre * 2 == s && j + 1 < n
  end
  false
end
