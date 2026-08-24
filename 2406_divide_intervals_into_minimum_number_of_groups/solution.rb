# LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

# @param {Integer[][]} intervals
# @return {Integer}
def min_groups(intervals)
  events = []
  intervals.each do |it|
    events << [it[0], 1]
    events << [it[1] + 1, -1]
  end
  events.sort_by! { |e| [e[0], e[1]] }
  cur = 0
  ans = 0
  events.each do |_, d|
    cur += d
    ans = cur if cur > ans
  end
  ans
end
