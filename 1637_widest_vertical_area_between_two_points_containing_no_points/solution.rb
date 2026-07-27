# LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

# @param {Integer[][]} points
# @return {Integer}
def max_width_of_vertical_area(points)
  xs = points.map(&:first).sort
  (0...(xs.length - 1)).map { |i| xs[i + 1] - xs[i] }.max
end
