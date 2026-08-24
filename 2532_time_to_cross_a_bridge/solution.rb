# LeetCode 2532 - Time to Cross a Bridge
# https://leetcode.com/problems/time-to-cross-a-bridge/

class MinHeap
  def initialize(arr = [])
    @a = arr.dup
    ((@a.length / 2) - 1).downto(0) { |i| down(i) }
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    top = @a[0]
    last = @a.pop
    unless @a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def peek
    @a[0]
  end

  def empty?
    @a.empty?
  end

  def length
    @a.length
  end

  def sum
    @a.sum
  end

  private

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if (@a[i] <=> @a[p]) >= 0

      @a[i], @a[p] = @a[p], @a[i]
      i = p
    end
  end

  def down(i)
    n = @a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && (@a[l] <=> @a[s]) < 0
      s = r if r < n && (@a[r] <=> @a[s]) < 0
      break if s == i

      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

# @param {Integer} n
# @param {Integer} k
# @param {Integer[][]} time
# @return {Integer}
def find_crossing_time(n, k, time)
  left = MinHeap.new
  right = MinHeap.new
  events = MinHeap.new
  ws = []
  k.times do |i|
    t = time[i]
    w = {
      idx: i,
      left_to_right: t[0],
      pick_old: t[1],
      right_to_left: t[2],
      put_new: t[3],
      efficiency: t[0] + t[2]
    }
    ws << w
    left.push([-w[:efficiency], -w[:idx], i])
  end
  cur = 0
  bridge_free = 0
  remain = n
  done = 0
  while done < n
    while !events.empty? && events.peek[0] <= cur
      _et, side, idx = events.pop
      w = ws[idx]
      if side == 0
        left.push([-w[:efficiency], -w[:idx], idx])
      else
        right.push([-w[:efficiency], -w[:idx], idx])
      end
    end
    if cur < bridge_free
      cur = bridge_free
      next
    end
    if !right.empty?
      _e, _id, idx = right.pop
      w = ws[idx]
      cur += w[:right_to_left]
      bridge_free = cur
      events.push([cur + w[:put_new], 0, w[:idx]])
      done += 1
      next
    end
    if !left.empty? && remain > 0
      _e, _id, idx = left.pop
      w = ws[idx]
      cur += w[:left_to_right]
      bridge_free = cur
      remain -= 1
      events.push([cur + w[:pick_old], 1, w[:idx]])
      next
    end
    break if events.empty?

    cur = events.peek[0]
  end
  cur
end
