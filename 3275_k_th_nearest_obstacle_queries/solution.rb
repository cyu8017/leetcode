# LeetCode 3275 - K-th Nearest Obstacle Queries
# https://leetcode.com/problems/k-th-nearest-obstacle-queries/

class MaxHeap
  def initialize
    @a = []
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def peek
    @a[0]
  end

  def size
    @a.length
  end

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if @a[i] <= @a[p]
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
      s = l if l < n && @a[l] > @a[s]
      s = r if r < n && @a[r] > @a[s]
      break if s == i
      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

# @param {Integer[][]} queries
# @param {Integer} k
# @return {Integer[]}
def results_array(queries, k)
  h = MaxHeap.new
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    d = q[0].abs + q[1].abs
    h.push(d)
    h.pop if h.size > k
    ans[i] = h.size < k ? -1 : h.peek
  end
  ans
end
