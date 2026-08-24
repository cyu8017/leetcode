# LeetCode 2034 - Stock Price Fluctuation
# https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice
  def initialize
    @latest_ts = 0
    @price_at = {}
    @max_heap = []
    @min_heap = []
  end

  def update(timestamp, price)
    @price_at[timestamp] = price
    @latest_ts = timestamp if timestamp >= @latest_ts
    heap_push(@max_heap, [-price, timestamp])
    heap_push(@min_heap, [price, timestamp])
    nil
  end

  def current
    @price_at[@latest_ts]
  end

  def maximum
    loop do
      price, ts = @max_heap[0]
      price = -price
      return price if @price_at[ts] == price

      heap_pop(@max_heap)
    end
  end

  def minimum
    loop do
      price, ts = @min_heap[0]
      return price if @price_at[ts] == price

      heap_pop(@min_heap)
    end
  end

  private

  def heap_push(heap, item)
    heap << item
    i = heap.length - 1
    while i.positive?
      p = (i - 1) / 2
      break if heap[p][0] < heap[i][0] || (heap[p][0] == heap[i][0] && heap[p][1] <= heap[i][1])

      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  def heap_pop(heap)
    return heap.pop if heap.length == 1

    top = heap[0]
    heap[0] = heap.pop
    i = 0
    loop do
      l = 2 * i + 1
      r = l + 1
      smallest = i
      smallest = l if l < heap.length && (heap[l][0] < heap[smallest][0] || (heap[l][0] == heap[smallest][0] && heap[l][1] < heap[smallest][1]))
      smallest = r if r < heap.length && (heap[r][0] < heap[smallest][0] || (heap[r][0] == heap[smallest][0] && heap[r][1] < heap[smallest][1]))
      break if smallest == i

      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
    top
  end
end
