# LeetCode 0435 - Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/

class Solution
  def erase_overlap_intervals(intervals)
    sorted = intervals.sort_by { |interval| interval[1] }
    removed = 0
    end_time = -Float::INFINITY

    sorted.each do |start, finish|
      if start < end_time
        removed += 1
      else
        end_time = finish
      end
    end

    removed
  end

  alias_method :eraseOverlapIntervals, :erase_overlap_intervals
end
