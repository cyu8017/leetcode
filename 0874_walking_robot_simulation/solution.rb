# LeetCode 0874 - Walking Robot Simulation
# https://leetcode.com/problems/walking-robot-simulation/

# @param {Integer[]} commands
# @param {Integer[][]} obstacles
# @return {Integer}
def robot_sim(commands, obstacles)
  blocked = {}
  obstacles.each { |x, y| blocked[[x, y]] = true }
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  x = 0
  y = 0
  d = 0
  best = 0
  commands.each do |cmd|
    if cmd == -1
      d = (d + 1) % 4
    elsif cmd == -2
      d = (d + 3) % 4
    else
      dx, dy = dirs[d]
      cmd.times do
        nx = x + dx
        ny = y + dy
        break if blocked[[nx, ny]]

        x = nx
        y = ny
      end
      best = [best, x * x + y * y].max
    end
  end
  best
end
