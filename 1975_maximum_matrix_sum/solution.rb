# LeetCode 1975 - Maximum Matrix Sum
# https://leetcode.com/problems/maximum-matrix-sum/

# @param {Integer[][]} matrix
# @return {Integer}
def max_matrix_sum(matrix)
  total = 0
  neg = 0
  mn = Float::INFINITY
  matrix.each do |row|
    row.each do |x|
      neg += 1 if x.negative?
      ax = x.abs
      total += ax
      mn = [mn, ax].min
    end
  end
  return total if neg.even?
  total - 2 * mn
end
