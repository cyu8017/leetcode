
# @param {Integer[][]} grid
# @param {Integer} r1
# @param {Integer} c1
# @param {Integer} r2
# @param {Integer} c2
# @return {Integer}
def find_shortest_path(grid, r1, c1, r2, c2)
  return 0 if r1 == r2 && c1 == c2

  m = grid.length
  n = grid[0].length
  dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  dist = Array.new(m) { Array.new(n, Float::INFINITY) }
  heap = []

  dist[r1][c1] = 0
  heap_push(heap, [0, r1, c1])

  until heap.empty?
    d, r, c = heap_pop(heap)
    return d if r == r2 && c == c2
    next if d > dist[r][c]

    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0

      nd = d + grid[nr][nc]
      if nd < dist[nr][nc]
        dist[nr][nc] = nd
        heap_push(heap, [nd, nr, nc])
      end
    end
  end
  -1
end

def heap_push(heap, item)
  heap << item
  i = heap.length - 1
  while i > 0
    p = (i - 1) / 2
    break if heap[p][0] <= heap[i][0]
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
    smallest = l if l < n && heap[l][0] < heap[smallest][0]
    smallest = r if r < n && heap[r][0] < heap[smallest][0]
    break if smallest == i
    heap[smallest], heap[i] = heap[i], heap[smallest]
    i = smallest
  end
  top
end
