# LeetCode 0715 - Range Module
# https://leetcode.com/problems/range-module/

class RangeModule
  def initialize
    @intervals = []
  end

  def add_range(left, right)
    new_intervals = []
    placed = false
    @intervals.each do |start, finish|
      if finish < left
        new_intervals << [start, finish]
      elsif right < start
        unless placed
          new_intervals << [left, right]
          placed = true
        end
        new_intervals << [start, finish]
      else
        left = [left, start].min
        right = [right, finish].max
      end
    end
    new_intervals << [left, right] unless placed
    @intervals = new_intervals
    nil
  end

  def query_range(left, right)
    i = bisect_right(left) - 1
    return false if i < 0

    @intervals[i][0] <= left && right <= @intervals[i][1]
  end

  def remove_range(left, right)
    new_intervals = []
    @intervals.each do |start, finish|
      if finish <= left || right <= start
        new_intervals << [start, finish]
      else
        new_intervals << [start, left] if start < left
        new_intervals << [right, finish] if right < finish
      end
    end
    @intervals = new_intervals
    nil
  end

  private

  def bisect_right(left)
    lo = 0
    hi = @intervals.length
    while lo < hi
      mid = (lo + hi) / 2
      if interval_less(@intervals[mid], [left, Float::INFINITY])
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  def interval_less(a, b)
    a[0] < b[0] || (a[0] == b[0] && a[1] < b[1])
  end
end
