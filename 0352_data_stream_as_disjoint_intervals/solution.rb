# LeetCode 0352 - Data Stream as Disjoint Intervals
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/

class SummaryRanges
  def initialize
    @intervals = []
  end

  def add_num(value)
    new_interval = [value, value]
    merged = []
    inserted = false

    @intervals.each do |interval|
      if interval[1] < value - 1
        merged << interval
      elsif interval[0] > value + 1
        unless inserted
          merged << new_interval
          inserted = true
        end
        merged << interval
      else
        new_interval[0] = [new_interval[0], interval[0]].min
        new_interval[1] = [new_interval[1], interval[1]].max
      end
    end

    merged << new_interval unless inserted
    @intervals = merged
  end

  def get_intervals
    @intervals
  end

  alias_method :addNum, :add_num
  alias_method :getIntervals, :get_intervals
end
