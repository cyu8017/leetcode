# LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
# https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_operations(grid)
  m = grid.length
  n = grid[0].length
  inf = 1 << 29
  f = Array.new(n) { Array.new(10, inf) }
  n.times do |i|
    cnt = Array.new(10, 0)
    m.times { |j| cnt[grid[j][i]] += 1 }
    if i == 0
      10.times { |j| f[i][j] = m - cnt[j] }
    else
      10.times do |j|
        10.times do |k|
          f[i][j] = [f[i][j], f[i - 1][k] + m - cnt[j]].min if j != k
        end
      end
    end
  end
  f[n - 1].min
end
