# LeetCode 1232 - Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

# @param {Integer[][]} coordinates
# @return {Boolean}
def check_straight_line(coordinates)
  x0, y0 = coordinates[0]
  dx = coordinates[1][0] - x0
  dy = coordinates[1][1] - y0
  coordinates[2..].all? { |x, y| (x - x0) * dy == (y - y0) * dx }
end
