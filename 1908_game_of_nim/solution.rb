# LeetCode 1908 - Game of Nim
# https://leetcode.com/problems/game-of-nim/

# @param {Integer[]} piles
# @return {Boolean}
def nim_game(piles)
  piles.reduce(0, :^) != 0
end
