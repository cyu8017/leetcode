# LeetCode 2054 - Two Best Non-Overlapping Events
# https://leetcode.com/problems/two-best-non-overlapping-events/

# @param {Integer[][]} events
# @return {Integer}
def max_two_events(events)
  events.sort_by! { |e| e[0] }
  n = events.length
  suffix = Array.new(n + 1, 0)
  (n - 1).downto(0) { |i| suffix[i] = [suffix[i + 1], events[i][2]].max }
  ans = 0
  n.times do |i|
    ans = [ans, events[i][2]].max
    lo = i + 1
    hi = n
    while lo < hi
      mid = (lo + hi) >> 1
      if events[mid][0] > events[i][1]
        hi = mid
      else
        lo = mid + 1
      end
    end
    ans = [ans, events[i][2] + suffix[lo]].max if lo < n
  end
  ans
end
