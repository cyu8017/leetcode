
class SeatManager
  # @param {Integer} n
  def initialize(n)
    @available = (1..n).to_a
  end

  # @return {Integer}
  def reserve
    heap_pop(@available)
  end

  # @param {Integer} seat_number
  # @return {Void}
  def unreserve(seat_number)
    heap_push(@available, seat_number)
    nil
  end

  private

  def heap_push(heap, item)
    heap << item
    i = heap.length - 1
    while i > 0
      p = (i - 1) / 2
      break if heap[p] <= heap[i]
      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  def heap_pop(heap)
    top = heap[0]
    last = heap.pop
    return top if heap.empty?
    heap[0] = last
    i = 0
    n = heap.length
    loop do
      l = 2 * i + 1
      r = 2 * i + 2
      smallest = i
      smallest = l if l < n && heap[l] < heap[smallest]
      smallest = r if r < n && heap[r] < heap[smallest]
      break if smallest == i
      heap[smallest], heap[i] = heap[i], heap[smallest]
      i = smallest
    end
    top
  end
end
