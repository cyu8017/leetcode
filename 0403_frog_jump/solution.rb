# LeetCode 0403 - Frog Jump
# https://leetcode.com/problems/frog-jump/

require "set"

class Solution
  def can_cross(stones)
    stone_set = stones.to_set
    jumps = stones.to_h { |stone| [stone, Set.new] }
    jumps[0].add(0)

    stones.each do |stone|
      jumps[stone].each do |jump|
        [jump - 1, jump, jump + 1].each do |next_jump|
          if next_jump > 0 && stone_set.include?(stone + next_jump)
            jumps[stone + next_jump].add(next_jump)
          end
        end
      end
    end

    !jumps[stones.last].empty?
  end

  alias_method :canCross, :can_cross
end
