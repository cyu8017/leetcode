# LeetCode 0057 - Insert Interval
# https://leetcode.com/problems/insert-interval/

# @param {Integer[][]} intervals
# @param {Integer[]} new_interval
# @return {Integer[][]}
def insert(intervals, new_interval)
  result = []
  i = 0

  while i < intervals.length && intervals[i][1] < new_interval[0]
    result << intervals[i]
    i += 1
  end

  while i < intervals.length && intervals[i][0] <= new_interval[1]
    new_interval[0] = [new_interval[0], intervals[i][0]].min
    new_interval[1] = [new_interval[1], intervals[i][1]].max
    i += 1
  end

  result << new_interval

  while i < intervals.length
    result << intervals[i]
    i += 1
  end

  result
end
