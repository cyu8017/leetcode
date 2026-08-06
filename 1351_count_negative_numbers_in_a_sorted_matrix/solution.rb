# LeetCode 1351 - Count Negative Numbers In A Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

def count_negatives(grid)
  grid.sum { |row| row.count(&:negative?) }
end
