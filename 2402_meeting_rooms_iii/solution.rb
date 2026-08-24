# LeetCode 2402 - Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/

# @param {Integer} n
# @param {Integer[][]} meetings
# @return {Integer}
def most_booked(n, meetings)
  meetings = meetings.sort_by { |x| x[0] }
  free = []
  busy = []
  push_free = lambda do |x|
    free << x
    i = free.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if free[p] <= free[i]
      free[p], free[i] = free[i], free[p]
      i = p
    end
  end
  pop_free = lambda do
    top = free[0]
    last = free.pop
    unless free.empty?
      free[0] = last
      i = 0
      loop do
        s = i
        l = i * 2 + 1
        r = i * 2 + 2
        s = l if l < free.length && free[l] < free[s]
        s = r if r < free.length && free[r] < free[s]
        break if s == i
        free[s], free[i] = free[i], free[s]
        i = s
      end
    end
    top
  end
  cmp_busy = lambda do |a, b|
    return a[0] - b[0] if a[0] != b[0]
    a[1] - b[1]
  end
  push_busy = lambda do |x|
    busy << x
    i = busy.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if cmp_busy.call(busy[p], busy[i]) <= 0
      busy[p], busy[i] = busy[i], busy[p]
      i = p
    end
  end
  pop_busy = lambda do
    top = busy[0]
    last = busy.pop
    unless busy.empty?
      busy[0] = last
      i = 0
      loop do
        s = i
        l = i * 2 + 1
        r = i * 2 + 2
        s = l if l < busy.length && cmp_busy.call(busy[l], busy[s]) < 0
        s = r if r < busy.length && cmp_busy.call(busy[r], busy[s]) < 0
        break if s == i
        busy[s], busy[i] = busy[i], busy[s]
        i = s
      end
    end
    top
  end
  (0...n).each { |i| push_free.call(i) }
  cnt = Array.new(n, 0)
  meetings.each do |start, finish|
    push_free.call(pop_busy.call[1]) while !busy.empty? && busy[0][0] <= start
    dur = finish - start
    if !free.empty?
      room = pop_free.call
      begin_t = start
    else
      top = pop_busy.call
      begin_t = top[0]
      room = top[1]
    end
    push_busy.call([begin_t + dur, room])
    cnt[room] += 1
  end
  ans = 0
  (1...n).each { |i| ans = i if cnt[i] > cnt[ans] }
  ans
end
