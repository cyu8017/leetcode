# LeetCode 1033 - Moving Stones Until Consecutive
# https://leetcode.com/problems/moving-stones-until-consecutive/

# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer[]}
def num_moves_stones(a, b, c)
  x, y, z = [a, b, c].sort
  min_moves = if z - x == 2
                0
              elsif y - x <= 2 || z - y <= 2
                1
              else
                2
              end
  [min_moves, z - x - 2]
end
