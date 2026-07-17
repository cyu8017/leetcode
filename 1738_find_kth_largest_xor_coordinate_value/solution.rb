# LeetCode 1738 - Find Kth Largest XOR Coordinate Value
# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

# @param {Integer[][]} matrix
# @param {Integer} k
# @return {Integer}
def kth_largest_value(matrix, k)
  rows = matrix.length
  cols = matrix[0].length
  pref = Array.new(rows + 1) { Array.new(cols + 1, 0) }
  values = []
  (1..rows).each do |r|
    (1..cols).each do |c|
      pref[r][c] = pref[r - 1][c] ^ pref[r][c - 1] ^ pref[r - 1][c - 1] ^ matrix[r - 1][c - 1]
      values << pref[r][c]
    end
  end
  values.sort! { |x, y| y <=> x }
  values[k - 1]
end
