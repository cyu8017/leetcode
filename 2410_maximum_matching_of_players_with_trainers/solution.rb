# LeetCode 2410 - Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

# @param {Integer[]} players
# @param {Integer[]} trainers
# @return {Integer}
def match_players_and_trainers(players, trainers)
  players = players.sort
  trainers = trainers.sort
  i = 0
  j = 0
  ans = 0
  while i < players.length && j < trainers.length
    if players[i] <= trainers[j]
      ans += 1
      i += 1
      j += 1
    else
      j += 1
    end
  end
  ans
end
