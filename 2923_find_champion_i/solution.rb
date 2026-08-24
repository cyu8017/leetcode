# LeetCode 2923 - Find Champion I
# https://leetcode.com/problems/find-champion-i/

# @param {Integer[][]} grid
# @return {Integer}
def find_champion(grid)
  n = grid.length
  (0...n).each do |i|
    win = true
    (0...n).each do |j|
      if i != j && grid[i][j] == 0
        win = false
        break
      end
    end
    return i if win
  end
  -1
end
