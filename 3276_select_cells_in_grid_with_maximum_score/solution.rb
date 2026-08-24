# LeetCode 3276 - Select Cells in Grid With Maximum Score
# https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

# @param {Integer[][]} grid
# @return {Integer}
def max_score(grid)
  m = grid.length
  vals = {}
  (0...m).each do |i|
    seen = {}
    grid[i].each do |v|
      next if seen[v]
      seen[v] = true
      vals[v] ||= []
      vals[v] << i
    end
  end
  arr = vals.keys.sort.reverse
  nn = 1 << m
  dp = Array.new(nn, 0)
  arr.each do |v|
    ndp = dp.dup
    vals[v].each do |r|
      bit = 1 << r
      (0...nn).each do |mask|
        next if (mask & bit) != 0
        cand = dp[mask] + v
        nmask = mask | bit
        ndp[nmask] = cand if cand > ndp[nmask]
      end
    end
    dp = ndp
  end
  dp.max
end
