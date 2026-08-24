# LeetCode 2352 - Equal Row and Column Pairs
# https://leetcode.com/problems/equal-row-and-column-pairs/

# @param {Integer[][]} grid
# @return {Integer}
def equal_pairs(grid)
  n = grid.length
  freq = Hash.new(0)
  (0...n).each { |i| freq[grid[i].dup] += 1 }
  ans = 0
  (0...n).each do |j|
    col = (0...n).map { |i| grid[i][j] }
    ans += freq[col]
  end
  ans
end
