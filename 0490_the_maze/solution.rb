# LeetCode 0490 - The Maze
# https://leetcode.com/problems/the-maze/

class Solution
  def has_path(maze, start, destination)
    rows = maze.length
    cols = maze[0].length
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = {}
    stack = [[start[0], start[1]]]

    until stack.empty?
      row, col = stack.pop
      next if visited[[row, col]]

      visited[[row, col]] = true
      return true if row == destination[0] && col == destination[1]

      directions.each do |dr, dc|
        nr = row
        nc = col
        while nr + dr >= 0 && nr + dr < rows && nc + dc >= 0 && nc + dc < cols && maze[nr + dr][nc + dc] == 0
          nr += dr
          nc += dc
        end
        stack << [nr, nc] unless visited[[nr, nc]]
      end
    end
    false
  end

  alias_method :hasPath, :has_path
end
