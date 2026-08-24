# LeetCode 0822 - Card Flipping Game
# https://leetcode.com/problems/card-flipping-game/

# @param {Integer[]} fronts
# @param {Integer[]} backs
# @return {Integer}
def flipgame(fronts, backs)
  same = {}
  fronts.zip(backs).each { |f, b| same[f] = true if f == b }
  best = Float::INFINITY
  (fronts + backs).each { |x| best = x if !same[x] && x < best }
  best == Float::INFINITY ? 0 : best
end
