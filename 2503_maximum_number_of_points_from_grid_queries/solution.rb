# LeetCode 2503 - Maximum Number of Points From Grid Queries
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

# @param {Integer[][]} grid
# @param {Integer[]} queries
# @return {Integer[]}
def max_points(grid, queries)
  m = grid.length
  n = grid[0].length
  order = (0...queries.length).to_a
  order.sort_by! { |i| queries[i] }
  ans = Array.new(queries.length, 0)
  visited = Array.new(m) { Array.new(n, false) }
  pq = [[grid[0][0], 0, 0]]
  visited[0][0] = true
  points = 0
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  heap_push = lambda do |heap, item|
    heap << item
    i = heap.length - 1
    while i > 0
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
      left = 2 * i + 1
      right = 2 * i + 2
      smallest = left if left < heap.length && heap[left] < heap[smallest]
      smallest = right if right < heap.length && heap[right] < heap[smallest]
      break if smallest == i

      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
    top
  end

  order.each do |qi|
    q = queries[qi]
    while !pq.empty? && pq[0][0] < q
      _, r, c = heap_pop.call(pq)
      points += 1
      dirs.each do |dr, dc|
        nr = r + dr
        nc = c + dc
        next if nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]

        visited[nr][nc] = true
        heap_push.call(pq, [grid[nr][nc], nr, nc])
      end
    end
    ans[qi] = points
  end
  ans
end
