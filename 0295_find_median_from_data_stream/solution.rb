# LeetCode 0295 - Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder
  def initialize
    @small = []
    @large = []
  end

  def addNum(num)
    push(@small, -num, true)
    push(@large, -pop(@small), false)
    push(@small, -pop(@large), true) if @large.length > @small.length
  end

  def findMedian
    return -@small[0].to_f if @small.length > @large.length

    (-@small[0] + @large[0]) / 2.0
  end

  private

  def push(heap, value, is_max_heap)
    heap << value
    bubble_up(heap, heap.length - 1, is_max_heap)
  end

  def pop(heap)
    top = heap[0]
    last = heap.pop
    if heap.length.positive?
      heap[0] = last
      bubble_down(heap, 0, heap.equal?(@small))
    end
    top
  end

  def bubble_up(heap, index, is_max_heap)
    while index.positive?
      parent = (index - 1) / 2
      break if is_max_heap ? heap[index] <= heap[parent] : heap[index] >= heap[parent]

      heap[index], heap[parent] = heap[parent], heap[index]
      index = parent
    end
  end

  def bubble_down(heap, index, is_max_heap)
    loop do
      target = index
      left = index * 2 + 1
      right = left + 1
      target = left if left < heap.length && (is_max_heap ? heap[left] > heap[target] : heap[left] < heap[target])
      target = right if right < heap.length && (is_max_heap ? heap[right] > heap[target] : heap[right] < heap[target])
      break if target == index

      heap[index], heap[target] = heap[target], heap[index]
      index = target
    end
  end
end
