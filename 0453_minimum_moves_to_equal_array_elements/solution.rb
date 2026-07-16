# LeetCode 0453 - Minimum Moves to Equal Array Elements
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution
  def min_moves(nums)
    minimum = nums.min
    nums.sum { |value| value - minimum }
  end

  alias_method :minMoves, :min_moves
end
