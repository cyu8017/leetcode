# LeetCode 0544 - Output Contest Matches
# https://leetcode.com/problems/output-contest-matches/

class Solution
  def find_contest_match(n)
    teams = (1..n).map(&:to_s)
    while teams.length > 1
      next_round = []
      half = teams.length / 2
      (0...half).each do |i|
        next_round << "(#{teams[i]},#{teams[-1 - i]})"
      end
      teams = next_round
    end
    teams[0]
  end

  alias_method :findContestMatch, :find_contest_match
end
