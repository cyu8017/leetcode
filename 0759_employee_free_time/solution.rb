# LeetCode 0759 - Employee Free Time
# https://leetcode.com/problems/employee-free-time/

class Interval
  attr_accessor :start, :end

  def initialize(start_val = 0, end_val = 0)
    @start = start_val
    @end = end_val
  end
end

# @param {Interval[][]} schedule
# @return {Integer[][]}
def employee_free_time(schedule)
  intervals = []
  schedule.each do |employee|
    employee.each do |item|
      if item.is_a?(Array)
        intervals << [item[0], item[1]]
      else
        intervals << [item.start, item.end]
      end
    end
  end

  intervals.sort_by! { |iv| iv[0] }
  merged = []
  intervals.each do |start, finish|
    if merged.empty? || merged[-1][1] < start
      merged << [start, finish]
    else
      merged[-1][1] = [merged[-1][1], finish].max
    end
  end

  (1...merged.length).map { |i| [merged[i - 1][1], merged[i][0]] }
end
