# LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

# @param {Integer[][]} matrix
# @return {Integer}
def max_equal_rows_after_flips(matrix)
  patterns = Hash.new(0)
  matrix.each do |row|
    base = row[0]
    key = row.map { |x| x ^ base }.join(",")
    patterns[key] += 1
  end
  patterns.values.max
end
