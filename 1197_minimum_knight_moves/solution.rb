# LeetCode 1197 - Minimum Knight Moves
# https://leetcode.com/problems/minimum-knight-moves/

# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def min_knight_moves(x, y)
  x = x.abs
  y = y.abs
  memo = {}
  dfs = nil
  dfs = lambda do |a, b|
    return 0 if a + b == 0
    return 2 if a + b == 2
    key = [a, b]
    return memo[key] if memo.key?(key)
    memo[key] = [dfs.call((a - 1).abs, (b - 2).abs), dfs.call((a - 2).abs, (b - 1).abs)].min + 1
  end
  dfs.call(x, y)
end
