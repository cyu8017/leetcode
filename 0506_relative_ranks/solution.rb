# LeetCode 0506 - Relative Ranks
# https://leetcode.com/problems/relative-ranks/

class Solution
  def find_relative_ranks(score)
    medals = { 1 => "Gold Medal", 2 => "Silver Medal", 3 => "Bronze Medal" }
    order = (0...score.length).sort_by { |index| -score[index] }
    result = Array.new(score.length, "")
    order.each_with_index do |index, rank|
      result[index] = medals.fetch(rank + 1, (rank + 1).to_s)
    end
    result
  end

  alias_method :findRelativeRanks, :find_relative_ranks
end
