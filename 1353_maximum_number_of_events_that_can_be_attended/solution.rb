# LeetCode 1353 - Maximum Number Of Events That Can Be Attended
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

def max_events(events)
  events = events.sort_by(&:first)
  heap = []
  i = 0
  day = 0
  answer = 0
  n = events.length
  while i < n || !heap.empty?
    day = events[i][0] if heap.empty? && i < n
    while i < n && events[i][0] <= day
      # push end day
      heap << events[i][1]
      heap.sort!
      i += 1
    end
    while !heap.empty? && heap[0] < day
      heap.shift
    end
    unless heap.empty?
      heap.shift
      answer += 1
    end
    day += 1
  end
  answer
end
