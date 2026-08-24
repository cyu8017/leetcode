# LeetCode 0741 - Cherry Pickup
# https://leetcode.com/problems/cherry-pickup/

# @param {Integer[][]} grid
# @return {Integer}
def cherry_pickup(grid)
  n = grid.length
  memo = {}
  dp = lambda do |r1, c1, c2|
    key = [r1, c1, c2]
    return memo[key] if memo.key?(key)

    r2 = r1 + c1 - c2
    if r1 >= n || c1 >= n || r2 >= n || c2 >= n || grid[r1][c1] == -1 || grid[r2][c2] == -1
      memo[key] = -10**9
      return memo[key]
    end
    if r1 == n - 1 && c1 == n - 1
      memo[key] = grid[r1][c1]
      return memo[key]
    end
    cherries = grid[r1][c1]
    cherries += grid[r2][c2] if r1 != r2 || c1 != c2
    cherries += [
      dp.call(r1 + 1, c1, c2),
      dp.call(r1, c1 + 1, c2),
      dp.call(r1 + 1, c1, c2 + 1),
      dp.call(r1, c1 + 1, c2 + 1)
    ].max
    memo[key] = cherries
    cherries
  end
  [0, dp.call(0, 0, 0)].max
end
