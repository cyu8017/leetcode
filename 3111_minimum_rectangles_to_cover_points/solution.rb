# LeetCode 3111 - Minimum Rectangles to Cover Points
# https://leetcode.com/problems/minimum-rectangles-to-cover-points/

# @param {Integer[][]} points
# @param {Integer} w
# @return {Integer}
def min_rectangles_to_cover_points(points, w)
  points = points.sort_by { |p| p[0] }
  ans = 0
  x1 = -1
  points.each do |p|
    if p[0] > x1
      ans += 1
      x1 = p[0] + w
    end
  end
  ans
end
