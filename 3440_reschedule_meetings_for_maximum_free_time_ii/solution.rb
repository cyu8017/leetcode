# LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

# @param {Integer} event_time
# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @return {Integer}
def max_free_time(event_time, start_time, end_time)
  n = start_time.length
  gaps = Array.new(n + 1, 0)
  gaps[0] = start_time[0]
  (1...n).each { |i| gaps[i] = start_time[i] - end_time[i - 1] }
  gaps[n] = event_time - end_time[n - 1]
  ans = 0
  gaps.each { |g| ans = g if g > ans }
  left_max = Array.new(n + 1, 0)
  right_max = Array.new(n + 1, 0)
  (0..(n)).each do |i|
    left_max[i] = gaps[i]
    left_max[i] = left_max[i - 1] if i > 0 && left_max[i - 1] > left_max[i]
  end
  n.downto(0) do |i|
    right_max[i] = gaps[i]
    right_max[i] = right_max[i + 1] if i < n && right_max[i + 1] > right_max[i]
  end
  (0...n).each do |i|
    dur = end_time[i] - start_time[i]
    merged = gaps[i] + gaps[i + 1]
    best_other = 0
    best_other = left_max[i - 1] if i > 0 && left_max[i - 1] > best_other
    best_other = right_max[i + 2] if i + 2 <= n && right_max[i + 2] > best_other
    cand = merged
    cand = merged + dur if best_other >= dur
    ans = cand if cand > ans
  end
  ans
end
