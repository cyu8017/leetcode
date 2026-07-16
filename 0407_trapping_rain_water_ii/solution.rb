# LeetCode 0407 - Trapping Rain Water II
# https://leetcode.com/problems/trapping-rain-water-ii/

class Solution
  def trap_rain_water(height_map)
    return 0 if height_map.nil? || height_map.empty? || height_map[0].empty?

    rows = height_map.length
    cols = height_map[0].length
    return 0 if rows < 3 || cols < 3

    visited = Array.new(rows) { Array.new(cols, false) }
    heap = []

    rows.times do |row|
      cols.times do |col|
        next unless row.zero? || row == rows - 1 || col.zero? || col == cols - 1

        heap_push(heap, [height_map[row][col], row, col])
        visited[row][col] = true
      end
    end

    trapped = 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    until heap.empty?
      height, row, col = heap_pop(heap)
      directions.each do |dr, dc|
        next_row = row + dr
        next_col = col + dc
        next if next_row.negative? || next_row >= rows || next_col.negative? || next_col >= cols
        next if visited[next_row][next_col]

        visited[next_row][next_col] = true
        next_height = height_map[next_row][next_col]
        trapped += [0, height - next_height].max
        heap_push(heap, [[height, next_height].max, next_row, next_col])
      end
    end

    trapped
  end

  alias_method :trapRainWater, :trap_rain_water

  private

  def heap_push(heap, item)
    heap << item
    index = heap.length - 1
    while index > 0
      parent = (index - 1) / 2
      break if heap[parent][0] <= heap[index][0]

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
      smallest = index
      left = index * 2 + 1
      right = index * 2 + 2
      smallest = left if left < heap.length && heap[left][0] < heap[smallest][0]
      smallest = right if right < heap.length && heap[right][0] < heap[smallest][0]
      break if smallest == index

      heap[smallest], heap[index] = heap[index], heap[smallest]
      index = smallest
    end
    top
  end
end
