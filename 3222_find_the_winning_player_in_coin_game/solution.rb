# LeetCode 3222 - Find the Winning Player in Coin Game
# https://leetcode.com/problems/find-the-winning-player-in-coin-game/

# @param {Integer} x
# @param {Integer} y
# @return {String}
def winning_player(x, y)
  k = [x / 2, y / 8].min
  x -= 2 * k
  y -= 8 * k
  return "Alice" if x > 0 && y >= 4
  "Bob"
end
