# LeetCode 0499 - The Maze III
# https://leetcode.com/problems/the-maze-iii/

class Solution
  def find_shortest_way(maze, ball, hole)
    rows = maze.length
    cols = maze[0].length
    hole_pos = [hole[0], hole[1]]
    directions = {
      "d" => [1, 0],
      "l" => [0, -1],
      "r" => [0, 1],
      "u" => [-1, 0]
    }

    roll = lambda do |row, col, dr, dc|
      distance = 0
      while row + dr >= 0 && row + dr < rows && col + dc >= 0 && col + dc < cols && maze[row + dr][col + dc] == 0
        row += dr
        col += dc
        distance += 1
        break if row == hole_pos[0] && col == hole_pos[1]
      end
      [row, col, distance]
    end

    best = {}
    heap = [[0, "", ball[0], ball[1]]]

    until heap.empty?
      heap.sort_by! { |dist, path, _, _| [dist, path] }
      dist, path, row, col = heap.shift
      state = [row, col]
      if best.key?(state) && [dist, path] >= best[state]
        next
      end
      best[state] = [dist, path]
      return path if row == hole_pos[0] && col == hole_pos[1]

      directions.each do |direction, (dr, dc)|
        next_row, next_col, traveled = roll.call(row, col, dr, dc)
        next if next_row == row && next_col == col

        new_dist = dist + traveled
        new_path = path + direction
        candidate = [new_dist, new_path]
        target = [next_row, next_col]
        if !best.key?(target) || candidate < best[target]
          heap << [new_dist, new_path, next_row, next_col]
        end
      end
    end

    "impossible"
  end

  alias_method :findShortestWay, :find_shortest_way
end
