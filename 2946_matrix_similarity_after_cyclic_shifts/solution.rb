# LeetCode 2946 - Matrix Similarity After Cyclic Shifts
# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

# @param {Integer[][]} mat
# @param {Integer} k
# @return {Boolean}
def are_similar(mat, k)
  m = mat.length
  n = mat[0].length
  m.times do |i|
    if i.even?
      shift = n - (k % n)
      shift = 0 if shift == n
    else
      shift = k % n
    end
    n.times do |j|
      return false if mat[i][j] != mat[i][(j + shift) % n]
    end
  end
  true
end
