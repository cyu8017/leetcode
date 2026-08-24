# LeetCode 2336 - Smallest Number in Infinite Set
# https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet
  def initialize
    @nxt = 1
    @added = {}
    @heap = []
  end

  def pop_smallest
    unless @heap.empty?
      x = _pop
      @added.delete(x)
      return x
    end
    val = @nxt
    @nxt += 1
    val
  end

  def add_back(num)
    if num < @nxt && !@added.key?(num)
      @added[num] = true
      _push(num)
    end
    nil
  end

  private

  def _bubble_up(i)
    while i > 0
      p = (i - 1) >> 1
      break if @heap[p] <= @heap[i]
      @heap[p], @heap[i] = @heap[i], @heap[p]
      i = p
    end
  end

  def _bubble_down(i)
    n = @heap.length
    loop do
      smallest = i
      l = i * 2 + 1
      r = i * 2 + 2
      smallest = l if l < n && @heap[l] < @heap[smallest]
      smallest = r if r < n && @heap[r] < @heap[smallest]
      break if smallest == i
      @heap[smallest], @heap[i] = @heap[i], @heap[smallest]
      i = smallest
    end
  end

  def _push(x)
    @heap << x
    _bubble_up(@heap.length - 1)
  end

  def _pop
    top = @heap[0]
    last = @heap.pop
    unless @heap.empty?
      @heap[0] = last
      _bubble_down(0)
    end
    top
  end
end
