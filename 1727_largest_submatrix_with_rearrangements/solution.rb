# LeetCode 1727 - Largest Submatrix With Rearrangements
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/

# @param {Integer[][]} matrix
# @return {Integer}
def largest_submatrix(matrix)
  n = matrix[0].length
  heights = Array.new(n, 0)
  best = 0
  matrix.each do |row|
    (0...n).each do |c|
      heights[c] = row[c] == 1 ? heights[c] + 1 : 0
    end
    sorted = heights.sort.reverse
    (1..n).each do |width|
      area = width * sorted[width - 1]
      best = area if area > best
    end
  end
  best
end
