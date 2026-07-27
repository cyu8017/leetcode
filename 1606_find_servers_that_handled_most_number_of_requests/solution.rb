# LeetCode 1606 - Find Servers That Handled Most Number of Requests
# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

class MinHeap1606
  def initialize
    @a = []
  end

  def empty?
    @a.empty?
  end

  def peek
    @a[0]
  end

  def push(x)
    @a << x
    i = @a.length - 1
    while i.positive?
      p = (i - 1) / 2
      break if (@a[p] <=> @a[i]) <= 0

      @a[p], @a[i] = @a[i], @a[p]
      i = p
    end
  end

  def pop
    return nil if @a.empty?

    top = @a[0]
    last = @a.pop
    return top if @a.empty?

    @a[0] = last
    i = 0
    loop do
      l = 2 * i + 1
      r = l + 1
      smallest = i
      smallest = l if l < @a.length && (@a[l] <=> @a[smallest]) < 0
      smallest = r if r < @a.length && (@a[r] <=> @a[smallest]) < 0
      break if smallest == i

      @a[i], @a[smallest] = @a[smallest], @a[i]
      i = smallest
    end
    top
  end
end

# @param {Integer} k
# @param {Integer[]} arrival
# @param {Integer[]} load
# @return {Integer[]}
def busiest_servers(k, arrival, load)
  free = MinHeap1606.new
  k.times { |i| free.push(i) }
  busy = MinHeap1606.new
  count = Array.new(k, 0)
  arrival.each_with_index do |t, i|
    length = load[i]
    while !busy.empty? && busy.peek[0] <= t
      _, server = busy.pop
      free.push(i + (server - i) % k)
    end
    next if free.empty?

    server = free.pop % k
    count[server] += 1
    busy.push([t + length, server])
  end
  best = count.max
  count.each_index.select { |i| count[i] == best }
end
