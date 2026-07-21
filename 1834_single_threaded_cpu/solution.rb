
# @param {Integer[][]} tasks
# @return {Integer[]}
def get_order(tasks)
  indexed = tasks.each_with_index.map { |task, idx| [idx, task] }
  indexed.sort_by! { |idx, task| [task[0], idx] }

  i = 0
  n = tasks.length
  heap = []
  time = 0
  order = []

  while i < n || !heap.empty?
    time = [time, indexed[i][1][0]].max if i < n && heap.empty?

    while i < n && indexed[i][1][0] <= time
      idx, task = indexed[i]
      heap_push(heap, [task[1], idx])
      i += 1
    end

    duration, idx = heap_pop(heap)
    time += duration
    order << idx
  end
  order
end

def heap_push(heap, item)
  heap << item
  i = heap.length - 1
  while i > 0
    p = (i - 1) / 2
    break if heap[p][0] < heap[i][0] || (heap[p][0] == heap[i][0] && heap[p][1] <= heap[i][1])
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
    if l < n && (heap[l][0] < heap[smallest][0] || (heap[l][0] == heap[smallest][0] && heap[l][1] < heap[smallest][1]))
      smallest = l
    end
    if r < n && (heap[r][0] < heap[smallest][0] || (heap[r][0] == heap[smallest][0] && heap[r][1] < heap[smallest][1]))
      smallest = r
    end
    break if smallest == i
    heap[smallest], heap[i] = heap[i], heap[smallest]
    i = smallest
  end
  top
end
