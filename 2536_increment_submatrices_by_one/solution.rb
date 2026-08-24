# LeetCode 2536 - Increment Submatrices by One
# https://leetcode.com/problems/increment-submatrices-by-one/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[][]}
def range_add_queries(n, queries)
  diff = Array.new(n + 1) { Array.new(n + 1, 0) }
  queries.each do |q|
    r1, c1, r2, c2 = q
    diff[r1][c1] += 1
    diff[r1][c2 + 1] -= 1
    diff[r2 + 1][c1] -= 1
    diff[r2 + 1][c2 + 1] += 1
  end
  mat = Array.new(n) { Array.new(n, 0) }
  n.times do |i|
    n.times do |j|
      v = diff[i][j]
      v += mat[i - 1][j] if i > 0
      v += mat[i][j - 1] if j > 0
      v -= mat[i - 1][j - 1] if i > 0 && j > 0
      mat[i][j] = v
    end
  end
  mat
end
