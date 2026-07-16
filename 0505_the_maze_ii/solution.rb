# LeetCode 0505 - The Maze II
# https://leetcode.com/problems/the-maze-ii/

class Solution
  def shortest_distance(maze, start, destination)
    rows = maze.length
    cols = maze[0].length
    target = [destination[0], destination[1]]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    best = {}
    heap = [[0, start[0], start[1]]]

    until heap.empty?
      heap.sort_by! { |dist, _, _| dist }
      dist, row, col = heap.shift
      return dist if row == target[0] && col == target[1]
      next if best.fetch([row, col], Float::INFINITY) <= dist

      best[[row, col]] = dist
      directions.each do |dr, dc|
        next_row = row
        next_col = col
        traveled = 0
        while next_row + dr >= 0 && next_row + dr < rows &&
              next_col + dc >= 0 && next_col + dc < cols &&
              maze[next_row + dr][next_col + dc] == 0
          next_row += dr
          next_col += dc
          traveled += 1
        end
        next if next_row == row && next_col == col

        new_dist = dist + traveled
        if new_dist < best.fetch([next_row, next_col], Float::INFINITY)
          heap << [new_dist, next_row, next_col]
        end
      end
    end

    -1
  end

  alias_method :shortestDistance, :shortest_distance
end
