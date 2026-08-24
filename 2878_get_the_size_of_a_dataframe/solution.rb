# LeetCode 2878 - Get the Size of a DataFrame
# https://leetcode.com/problems/get-the-size-of-a-dataframe/

# @param {Object} players
# @return {Integer[]}
def get_dataframe_size(players)
  return [0, 0] if !players || (players.respond_to?(:empty?) && players.empty?)

  rows = players.length
  first = players[0]
  cols = first.is_a?(Array) ? first.length : first.keys.length
  [rows, cols]
end
