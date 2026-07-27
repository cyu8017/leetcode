# LeetCode 1626 - Best Team With No Conflicts
# https://leetcode.com/problems/best-team-with-no-conflicts/

# @param {Integer[]} scores
# @param {Integer[]} ages
# @return {Integer}
def best_team_score(scores, ages)
  players = ages.zip(scores).sort
  dp = Array.new(players.length, 0)
  players.each_with_index do |(_, score), i|
    best = 0
    (0...i).each do |j|
      best = [best, dp[j]].max if players[j][1] <= score
    end
    dp[i] = score + best
  end
  dp.max || 0
end
