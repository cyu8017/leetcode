# LeetCode 1252 - Cells with Odd Values in a Matrix
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} indices
# @return {Integer}
def odd_cells(m, n, indices)
  rows = Array.new(m, 0)
  cols = Array.new(n, 0)
  indices.each do |r, c|
    rows[r] ^= 1
    cols[c] ^= 1
  end
  ans = 0
  m.times { |r| n.times { |c| ans += 1 if (rows[r] ^ cols[c]) == 1 } }
  ans
end
