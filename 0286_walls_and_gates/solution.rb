# LeetCode 0286 - Walls and Gates
# https://leetcode.com/problems/walls-and-gates/

class Solution
  def wallsAndGates(rooms)
    return if rooms.nil? || rooms.empty?

    rows = rooms.length
    cols = rooms[0].length
    queue = []
    (0...rows).each do |row|
      (0...cols).each do |col|
        queue << [row, col] if rooms[row][col] == 0
      end
    end
    until queue.empty?
      row, col = queue.shift
      [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
        nr = row + dr
        nc = col + dc
        next unless nr.between?(0, rows - 1) && nc.between?(0, cols - 1)
        next unless rooms[nr][nc] == 2_147_483_647

        rooms[nr][nc] = rooms[row][col] + 1
        queue << [nr, nc]
      end
    end
  end
end
