# LeetCode 1314 - Matrix Block Sum
# https://leetcode.com/problems/matrix-block-sum/

def matrix_block_sum(mat, k)
  m = mat.length
  n = mat[0].length
  prefix = Array.new(m + 1) { Array.new(n + 1, 0) }
  m.times do |r|
    n.times do |c|
      prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
    end
  end
  answer = Array.new(m) { Array.new(n, 0) }
  m.times do |r|
    n.times do |c|
      r1 = [0, r - k].max
      c1 = [0, c - k].max
      r2 = [m, r + k + 1].min
      c2 = [n, c + k + 1].min
      answer[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]
    end
  end
  answer
end
