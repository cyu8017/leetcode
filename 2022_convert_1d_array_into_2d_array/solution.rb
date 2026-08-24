# LeetCode 2022 - Convert 1D Array Into 2D Array
# https://leetcode.com/problems/convert-1d-array-into-2d-array/

# @param {Integer[]} original
# @param {Integer} m
# @param {Integer} n
# @return {Integer[][]}
def construct2_d_array(original, m, n)
  return [] if original.length != m * n

  ans = Array.new(m) { Array.new(n, 0) }
  m.times do |i|
    n.times { |j| ans[i][j] = original[i * n + j] }
  end
  ans
end
