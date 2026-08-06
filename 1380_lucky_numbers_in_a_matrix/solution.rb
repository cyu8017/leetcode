# LeetCode 1380 - Lucky Numbers In A Matrix
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

def lucky_numbers(matrix)
  mins = {}
  matrix.each { |row| mins[row.min] = true }
  maxs = {}
  matrix.transpose.each { |col| maxs[col.max] = true }
  mins.keys.select { |x| maxs[x] }
end
