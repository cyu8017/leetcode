# LeetCode 1510 - Stone Game IV
# https://leetcode.com/problems/stone-game-iv/

# @param {Integer} n
# @return {Boolean}
def winner_square_game(n)
  win = Array.new(n + 1, false)
  (1..n).each do |value|
    root = 1
    while root * root <= value
      unless win[value - root * root]
        win[value] = true
        break
      end
      root += 1
    end
  end
  win[n]
end
