# LeetCode 0489 - Robot Room Cleaner
# https://leetcode.com/problems/robot-room-cleaner/

class Solution
  def clean_room(robot)
    visited = {}
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    backtrack = lambda do |row, col, direction|
      robot.clean
      4.times do |step|
        d = (direction + step) % 4
        dr, dc = directions[d]
        next_row = row + dr
        next_col = col + dc
        key = [next_row, next_col, d]
        if !visited[key] && robot.move
          visited[key] = true
          backtrack.call(next_row, next_col, d)
          robot.turnRight
          robot.turnRight
          robot.move
          robot.turnRight
          robot.turnRight
        end
        robot.turnRight
      end
    end

    visited[[0, 0, 0]] = true
    backtrack.call(0, 0, 0)
  end

  alias_method :cleanRoom, :clean_room
end
