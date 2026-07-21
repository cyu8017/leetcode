# LeetCode 1882 - Process Tasks Using Servers
# https://leetcode.com/problems/process-tasks-using-servers/

# @param {Integer[]} servers
# @param {Integer[]} tasks
# @return {Integer[]}
def assign_tasks(servers, tasks)
  available = []
  servers.each_with_index { |weight, index| heap_push2(available, [weight, index]) }
  busy = []
  answer = []
  time = 0

  tasks.each_with_index do |task, moment|
    time = [time, moment].max
    while !busy.empty? && busy[0][0] <= time
      _, weight, index = heap_pop2(busy)
      heap_push2(available, [weight, index])
    end

    while available.empty?
      time = busy[0][0]
      while !busy.empty? && busy[0][0] <= time
        _, weight, index = heap_pop2(busy)
        heap_push2(available, [weight, index])
      end
    end

    weight, index = heap_pop2(available)
    heap_push2(busy, [time + task, weight, index])
    answer << index
  end

  answer
end

def heap_push2(heap, item)
  heap << item
  index = heap.length - 1
  while index > 0
    parent = (index - 1) / 2
    break if cmp_tuple(heap[parent], heap[index]) <= 0

    heap[parent], heap[index] = heap[index], heap[parent]
    index = parent
  end
end

def heap_pop2(heap)
  top = heap[0]
  last = heap.pop
  return top if heap.empty?

  heap[0] = last
  index = 0
  loop do
    left = index * 2 + 1
    right = left + 1
    smallest = index
    smallest = left if left < heap.length && cmp_tuple(heap[left], heap[smallest]) < 0
    smallest = right if right < heap.length && cmp_tuple(heap[right], heap[smallest]) < 0
    break if smallest == index

    heap[smallest], heap[index] = heap[index], heap[smallest]
    index = smallest
  end
  top
end

def cmp_tuple(a, b)
  a.length.times do |i|
    return a[i] <=> b[i] if a[i] != b[i]
  end
  0
end
