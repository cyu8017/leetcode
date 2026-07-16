# LeetCode 0462 - Minimum Moves to Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution
  def min_moves2(nums)
    sorted = nums.sort
    median = sorted[sorted.length / 2]
    nums.sum { |value| (value - median).abs }
  end

  alias_method :minMoves2, :min_moves2
end
