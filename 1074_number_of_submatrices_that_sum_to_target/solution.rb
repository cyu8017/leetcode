# LeetCode 1074 - Number of Submatrices That Sum to Target
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Integer}
def num_submatrix_sum_target(matrix, target)
  rows = matrix.length
  cols = matrix[0].length
  ans = 0
  (0...cols).each do |left|
    row_sum = Array.new(rows, 0)
    (left...cols).each do |right|
      rows.times { |r| row_sum[r] += matrix[r][right] }
      prefix = 0
      seen = Hash.new(0)
      seen[0] = 1
      row_sum.each do |val|
        prefix += val
        ans += seen[prefix - target]
        seen[prefix] += 1
      end
    end
  end
  ans
end
