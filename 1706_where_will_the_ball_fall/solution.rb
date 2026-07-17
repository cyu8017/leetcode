# LeetCode 1706 - Where Will the Ball Fall
# https://leetcode.com/problems/where-will-the-ball-fall/

# @param {Integer[][]} grid
# @return {Integer[]}
def find_ball(grid)
  m = grid.length
  n = grid[0].length
  ans = []
  (0...n).each do |start|
    col = start
    (0...m).each do |row|
      nxt = col + grid[row][col]
      if nxt < 0 || nxt == n || grid[row][nxt] != grid[row][col]
        col = -1
        break
      end
      col = nxt
    end
    ans << col
  end
  ans
end
