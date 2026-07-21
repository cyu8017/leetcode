# LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

# @param {Integer} n
# @param {Integer} first_player
# @param {Integer} second_player
# @return {Integer[]}
def earliest_and_latest(n, first_player, second_player)
  first = first_player
  second = second_player
  memo = {}

  dfs = lambda do |players|
    return memo[players] if memo.key?(players)

    count = players.length
    first_index = players.index(first)
    second_index = players.index(second)
    if first_index + second_index == count - 1
      return memo[players] = [1, 1]
    end

    choices = []
    (0...count / 2).each do |index|
      left = players[index]
      right = players[count - 1 - index]
      if left == first || left == second
        choices << [left]
      elsif right == first || right == second
        choices << [right]
      else
        choices << [left, right]
      end
    end
    choices << [players[count / 2]] if count.odd?

    earliest = 10**9
    latest = 0

    enumerate = lambda do |idx, picks|
      if idx == choices.length
        winners = picks.sort
        early, late = dfs.call(winners)
        earliest = [earliest, early + 1].min
        latest = [latest, late + 1].max
        return
      end
      choices[idx].each do |player|
        picks << player
        enumerate.call(idx + 1, picks)
        picks.pop
      end
    end

    enumerate.call(0, [])
    memo[players] = [earliest, latest]
  end

  dfs.call((1..n).to_a)
end
