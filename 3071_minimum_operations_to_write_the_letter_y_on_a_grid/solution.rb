# LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_operations_to_write_y(grid)
  n = grid.length
  cnt1 = [0, 0, 0]
  cnt2 = [0, 0, 0]
  n.times do |i|
    n.times do |j|
      x = grid[i][j]
      a = i == j && i <= n / 2
      b = i + j == n - 1 && i <= n / 2
      c = j == n / 2 && i >= n / 2
      if a || b || c
        cnt1[x] += 1
      else
        cnt2[x] += 1
      end
    end
  end
  ans = n * n
  3.times do |i|
    3.times do |j|
      ans = [ans, n * n - cnt1[i] - cnt2[j]].min if i != j
    end
  end
  ans
end
