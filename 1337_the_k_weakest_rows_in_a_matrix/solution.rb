# LeetCode 1337 - The K Weakest Rows In A Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

def k_weakest_rows(mat, k)
  (0...mat.length).sort_by { |i| [mat[i].sum, i] }.first(k)
end
