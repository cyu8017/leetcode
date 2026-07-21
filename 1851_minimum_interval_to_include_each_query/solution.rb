# LeetCode 1851 - Minimum Interval to Include Each Query
# https://leetcode.com/problems/minimum-interval-to-include-each-query/

# @param {Integer[][]} intervals
# @param {Integer[]} queries
# @return {Integer[]}
def min_interval(intervals, queries)
  intervals = intervals.sort_by(&:first)
  indexed = queries.each_with_index.map { |q, i| [q, i] }.sort_by(&:first)
  heap = []
  answer = Array.new(queries.length, -1)
  interval_idx = 0

  indexed.each do |query, query_idx|
    while interval_idx < intervals.length && intervals[interval_idx][0] <= query
      left, right = intervals[interval_idx]
      heap_push(heap, [right - left + 1, right])
      interval_idx += 1
    end

    while !heap.empty? && heap[0][1] < query
      heap_pop(heap)
    end

    answer[query_idx] = heap[0][0] unless heap.empty?
  end

  answer
end

def heap_push(heap, item)
  heap << item
  index = heap.length - 1
  while index > 0
    parent = (index - 1) / 2
    break if heap[parent][0] < heap[index][0] || (heap[parent][0] == heap[index][0] && heap[parent][1] <= heap[index][1])
    heap[parent], heap[index] = heap[index], heap[parent]
    index = parent
  end
end

def heap_pop(heap)
  top = heap[0]
  last = heap.pop
  return top if heap.empty?

  heap[0] = last
  index = 0
  loop do
    left = index * 2 + 1
    right = left + 1
    smallest = index
    smallest = left if left < heap.length && (heap[left][0] < heap[smallest][0] || (heap[left][0] == heap[smallest][0] && heap[left][1] < heap[smallest][1]))
    smallest = right if right < heap.length && (heap[right][0] < heap[smallest][0] || (heap[right][0] == heap[smallest][0] && heap[right][1] < heap[smallest][1]))
    break if smallest == index

    heap[smallest], heap[index] = heap[index], heap[smallest]
    index = smallest
  end
  top
end
