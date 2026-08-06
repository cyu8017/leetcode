# LeetCode 1942 - The Number of the Smallest Unoccupied Chair
# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

# @param {Integer[][]} times
# @param {Integer} target_friend
# @return {Integer}
def smallest_chair(times, target_friend)
  order = (0...times.length).sort_by { |i| times[i][0] }
  free = []
  next_chair = 0
  leaving = []

  heap_push = lambda do |heap, item|
    heap << item
    i = heap.length - 1
    while i.positive?
      p = (i - 1) / 2
      break if heap[p] <= heap[i]
      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  heap_pop = lambda do |heap|
    top = heap[0]
    last = heap.pop
    return top if heap.empty?
    heap[0] = last
    i = 0
    loop do
      smallest = i
      l = 2 * i + 1
      r = 2 * i + 2
      smallest = l if l < heap.length && heap[l] < heap[smallest]
      smallest = r if r < heap.length && heap[r] < heap[smallest]
      break if smallest == i
      heap[smallest], heap[i] = heap[i], heap[smallest]
      i = smallest
    end
    top
  end

  order.each do |i|
    arr, leave = times[i]
    while !leaving.empty? && leaving[0][0] <= arr
      heap_push.call(free, heap_pop.call(leaving)[1])
    end
    if free.empty?
      chair = next_chair
      next_chair += 1
    else
      chair = heap_pop.call(free)
    end
    return chair if i == target_friend
    heap_push.call(leaving, [leave, chair])
  end
  -1
end
