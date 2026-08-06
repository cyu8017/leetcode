# LeetCode 1266 - Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/

# @param {Integer[][]} points
# @return {Integer}
def min_time_to_visit_all_points(points)
  points.each_cons(2).sum { |a, b| [(a[0] - b[0]).abs, (a[1] - b[1]).abs].max }
end
