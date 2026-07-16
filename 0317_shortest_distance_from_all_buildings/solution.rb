# LeetCode 0317 - Shortest Distance from All Buildings
# https://leetcode.com/problems/shortest-distance-from-all-buildings/

class Solution
  def shortestDistance(grid)
    return -1 if grid.empty?

    rows = grid.length
    cols = grid[0].length
    buildings = grid.flatten.count(1)
    distances = Array.new(rows) { Array.new(cols, 0) }
    reach = Array.new(rows) { Array.new(cols, 0) }
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    (0...rows).each do |row|
      (0...cols).each do |col|
        next unless grid[row][col] == 1

        queue = [[row, col, 0]]
        visited = { [row, col] => true }
        until queue.empty?
          current_row, current_col, distance = queue.shift
          directions.each do |dr, dc|
            nr = current_row + dr
            nc = current_col + dc
            next unless nr.between?(0, rows - 1) && nc.between?(0, cols - 1)
            next unless grid[nr][nc] == 0
            next if visited[[nr, nc]]

            visited[[nr, nc]] = true
            distances[nr][nc] += distance + 1
            reach[nr][nc] += 1
            queue << [nr, nc, distance + 1]
          end
        end
      end
    end

    best = Float::INFINITY
    (0...rows).each do |row|
      (0...cols).each do |col|
        if grid[row][col] == 0 && reach[row][col] == buildings
          best = [best, distances[row][col]].min
        end
      end
    end
    best == Float::INFINITY ? -1 : best
  end
end
