# LeetCode 0436 - Find Right Interval
# https://leetcode.com/problems/find-right-interval/

class Solution
  def find_right_interval(intervals)
    indexed = intervals.each_with_index.map { |(start, _), index| [start, index] }.sort
    starts = indexed.map(&:first)
    intervals.map do |start, finish|
      position = starts.bsearch_index { |value| value >= finish }
      position.nil? ? -1 : indexed[position][1]
    end
  end

  alias_method :findRightInterval, :find_right_interval
end
