# LeetCode 2017 - Grid Game
# https://leetcode.com/problems/grid-game/

# @param {Integer[][]} grid
# @return {Integer}
def grid_game(grid)
  n = grid[0].length
  top = grid[0].sum
  bottom = 0
  ans = 10**18
  n.times do |i|
    top -= grid[0][i]
    ans = [ans, [top, bottom].max].min
    bottom += grid[1][i]
  end
  ans
end
