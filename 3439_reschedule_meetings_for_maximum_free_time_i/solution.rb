# LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

# @param {Integer} event_time
# @param {Integer} k
# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @return {Integer}
def max_free_time(event_time, k, start_time, end_time)
  n = start_time.length
  gaps = Array.new(n + 1, 0)
  gaps[0] = start_time[0]
  (1...n).each { |i| gaps[i] = start_time[i] - end_time[i - 1] }
  gaps[n] = event_time - end_time[n - 1]
  window = k + 1
  s = 0
  (0...[window, gaps.length].min).each { |i| s += gaps[i] }
  ans = s
  (window...gaps.length).each do |i|
    s += gaps[i] - gaps[i - window]
    ans = s if s > ans
  end
  ans
end
