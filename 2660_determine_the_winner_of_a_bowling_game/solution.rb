# LeetCode 2660 - Determine the Winner of a Bowling Game
# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

# @param {Integer[]} player1
# @param {Integer[]} player2
# @return {Integer}
def is_winner(player1, player2)
  score = lambda do |p|
    s = 0
    p.each_with_index do |pins, i|
      mul = 1
      mul = 2 if (i > 0 && p[i - 1] == 10) || (i > 1 && p[i - 2] == 10)
      s += mul * pins
    end
    s
  end
  a = score.call(player1)
  b = score.call(player2)
  return 1 if a > b
  return 2 if b > a

  0
end
