# LeetCode 0778 - Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/

# @param {Integer[][]} grid
# @return {Integer}
def swim_in_water(grid)
  n = grid.length
  heap = [[grid[0][0], 0, 0]]
  seen = { [0, 0] => true }

  heap_push = lambda do |item|
    heap << item
    i = heap.length - 1
    while i > 0
      parent = (i - 1) / 2
      break if heap[parent][0] <= heap[i][0]

      heap[parent], heap[i] = heap[i], heap[parent]
      i = parent
    end
  end

  heap_pop = lambda do
    last = heap.pop
    return last if heap.empty?

    top = heap[0]
    heap[0] = last
    i = 0
    loop do
      smallest = i
      left = 2 * i + 1
      right = 2 * i + 2
      smallest = left if left < heap.length && heap[left][0] < heap[smallest][0]
      smallest = right if right < heap.length && heap[right][0] < heap[smallest][0]
      break if smallest == i

      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
    top
  end

  until heap.empty?
    time, r, c = heap_pop.call
    return time if r == n - 1 && c == n - 1

    [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]].each do |nr, nc|
      next unless nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[[nr, nc]]

      seen[[nr, nc]] = true
      heap_push.call([[time, grid[nr][nc]].max, nr, nc])
    end
  end
  -1
end
