# LeetCode 3508 - Implement Router
# https://leetcode.com/problems/implement-router/

class Router
  def initialize(memory_limit)
    @lim = memory_limit
    @vis = {}
    @q = []
    @idx = {}
    @d = {}
  end

  def f(a, b, c)
    (a << 46) | (b << 29) | c
  end

  def add_packet(source, destination, timestamp)
    x = f(source, destination, timestamp)
    return false if @vis[x]
    @vis[x] = true
    forward_packet if @q.length >= @lim
    @q << [source, destination, timestamp]
    @d[destination] ||= []
    @d[destination] << timestamp
    true
  end

  def forward_packet
    return [] if @q.empty?
    packet = @q.shift
    s, dest, t = packet[0], packet[1], packet[2]
    @vis.delete(f(s, dest, t))
    @idx[dest] = (@idx[dest] || 0) + 1
    [s, dest, t]
  end

  def get_count(destination, start_time, end_time)
    ls = @d[destination]
    return 0 unless ls
    k = @idx[destination] || 0
    lower_bound(ls, k, end_time + 1) - lower_bound(ls, k, start_time)
  end

  def lower_bound(a, frm, target)
    lo = frm
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
end
