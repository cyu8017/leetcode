# LeetCode 1222 - Queens That Can Attack the King
# https://leetcode.com/problems/queens-that-can-attack-the-king/

require "set"

# @param {Integer[][]} queens
# @param {Integer[]} king
# @return {Integer[][]}
def queens_attackthe_king(queens, king)
  occupied = Set.new(queens.map(&:dup))
  answer = []
  [-1, 0, 1].each do |dr|
    [-1, 0, 1].each do |dc|
      next if dr == 0 && dc == 0
      r = king[0] + dr
      c = king[1] + dc
      while r >= 0 && r < 8 && c >= 0 && c < 8
        if occupied.include?([r, c])
          answer << [r, c]
          break
        end
        r += dr
        c += dc
      end
    end
  end
  answer
end
