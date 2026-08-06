# LeetCode 1366 - Rank Teams By Votes
# https://leetcode.com/problems/rank-teams-by-votes/

def rank_teams(votes)
  m = votes[0].length
  count = {}
  votes[0].each_char { |c| count[c] = Array.new(m, 0) }
  votes.each do |v|
    v.each_char.with_index { |c, i| count[c][i] += 1 }
  end
  count.keys.sort_by { |c| [count[c].map { |x| -x }, c] }.join
end
