# LeetCode 1872 - Stone Game VIII
# https://leetcode.com/problems/stone-game-viii/

# @param {Integer[]} stones
# @return {Integer}
def stone_game_v_i_i_i(stones)
  n = stones.length
  (1...n).each { |i| stones[i] += stones[i - 1] }

  score = stones[-1]
  (n - 2).downto(1) do |i|
    score = [stones[i] - score, score].max
  end
  score
end
