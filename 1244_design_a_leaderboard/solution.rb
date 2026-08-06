# LeetCode 1244 - Design A Leaderboard
# https://leetcode.com/problems/design-a-leaderboard/

class Leaderboard
  def initialize
    @scores = Hash.new(0)
  end

  def add_score(player_id, score)
    @scores[player_id] += score
  end

  def top(k)
    @scores.values.sort.reverse.take(k).sum
  end

  def reset(player_id)
    @scores.delete(player_id)
  end
end
