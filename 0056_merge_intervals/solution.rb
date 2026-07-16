# LeetCode 0056 - Merge Intervals
# https://leetcode.com/problems/merge-intervals/

# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
  intervals.sort_by { |interval| interval[0] }
  merged = [intervals[0]]

  intervals[1..].each do |start, finish|
    last = merged[-1]

    if start <= last[1]
      last[1] = [last[1], finish].max
    else
      merged << [start, finish]
    end
  end

  merged
end
