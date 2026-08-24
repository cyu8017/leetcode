# LeetCode 0703 - Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest
  def initialize(k, nums)
    @k = k
    @heap = nums.dup
    heapify
    heap_pop while @heap.length > @k
  end

  def add(val)
    heap_push(val)
    heap_pop if @heap.length > @k
    @heap[0]
  end

  private

  def heapify
    return if @heap.empty?

    ((@heap.length / 2) - 1).downto(0) { |i| sift_down(i) }
  end

  def heap_push(val)
    @heap << val
    sift_up(@heap.length - 1)
  end

  def heap_pop
    last = @heap.pop
    return last if @heap.empty?

    top = @heap[0]
    @heap[0] = last
    sift_down(0)
    top
  end

  def sift_up(i)
    while i > 0
      parent = (i - 1) / 2
      break if @heap[parent] <= @heap[i]

      @heap[parent], @heap[i] = @heap[i], @heap[parent]
      i = parent
    end
  end

  def sift_down(i)
    n = @heap.length
    loop do
      smallest = i
      left = 2 * i + 1
      right = 2 * i + 2
      smallest = left if left < n && @heap[left] < @heap[smallest]
      smallest = right if right < n && @heap[right] < @heap[smallest]
      break if smallest == i

      @heap[i], @heap[smallest] = @heap[smallest], @heap[i]
      i = smallest
    end
  end
end
