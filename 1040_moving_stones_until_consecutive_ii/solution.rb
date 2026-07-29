# LeetCode 1040 - Moving Stones Until Consecutive II
# https://leetcode.com/problems/moving-stones-until-consecutive-ii/

# @param {Integer[]} stones
# @return {Integer[]}
def num_moves_stones_ii(stones)
  stones = stones.sort
  n = stones.length
  max_moves = [stones[-1] - stones[1] - n + 2, stones[-2] - stones[0] - n + 2].max
  min_moves = max_moves
  i = 0
  n.times do |j|
    i += 1 while stones[j] - stones[i] + 1 > n
    inside = j - i + 1
    min_moves = if inside == n - 1 && stones[j] - stones[i] + 1 == n - 1
                  [min_moves, 2].min
                else
                  [min_moves, n - inside].min
                end
  end
  [min_moves, max_moves]
end
