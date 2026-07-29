# LeetCode 1041 - Robot Bounded In Circle
# https://leetcode.com/problems/robot-bounded-in-circle/

# @param {String} instructions
# @return {Boolean}
def is_robot_bounded(instructions)
  x = y = 0
  dx = 0
  dy = 1
  instructions.each_char do |ch|
    case ch
    when "G"
      x += dx
      y += dy
    when "L"
      dx, dy = -dy, dx
    else
      dx, dy = dy, -dx
    end
  end
  (x.zero? && y.zero?) || !(dx.zero? && dy == 1)
end
