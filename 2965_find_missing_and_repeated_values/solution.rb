# LeetCode 2965 - Find Missing and Repeated Values
# https://leetcode.com/problems/find-missing-and-repeated-values/

# @param {Integer[][]} grid
# @return {Integer[]}
def find_missing_and_repeated_values(grid)
  n = grid.length
  freq = Array.new(n * n + 1, 0)
  n.times { |i| n.times { |j| freq[grid[i][j]] += 1 } }
  rep = 0
  miss = 0
  (1..n * n).each do |i|
    rep = i if freq[i] == 2
    miss = i if freq[i] == 0
  end
  [rep, miss]
end
