# LeetCode 0963 - Minimum Area Rectangle II
# https://leetcode.com/problems/minimum-area-rectangle-ii/

# @param {Integer[][]} points
# @return {Float}
def min_area_free_rect(points)
  pts = points.map { |x, y| Complex(x, y) }
  groups = Hash.new { |h, k| h[k] = [] }
  pts.combination(2).each do |p, q|
    center = [((p.real + q.real) / 2.0), (p.imag + q.imag) / 2.0]
    dist = (p - q).abs**2
    groups[[center, dist]] << [p, q]
  end
  ans = Float::INFINITY
  groups.each_value do |pairs|
    pairs.combination(2).each do |(p1, q1), (p2, q2)|
      area = (p1 - p2).abs * (p1 - q2).abs
      ans = area if area > 0 && area < ans
    end
  end
  ans == Float::INFINITY ? 0.0 : ans
end
