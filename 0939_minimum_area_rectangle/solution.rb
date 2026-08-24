# LeetCode 0939 - Minimum Area Rectangle
# https://leetcode.com/problems/minimum-area-rectangle/

# @param {Integer[][]} points
# @return {Integer}
def min_area_rect(points)
  by_x = Hash.new { |h, k| h[k] = [] }
  points.each { |x, y| by_x[x] << y }
  last = {}
  ans = Float::INFINITY
  by_x.keys.sort.each do |x|
    ys = by_x[x].sort
    ys.each_index do |i|
      ((i + 1)...ys.length).each do |j|
        y1 = ys[i]
        y2 = ys[j]
        key = [y1, y2]
        ans = [ans, (x - last[key]).abs * (y2 - y1).abs].min if last.key?(key)
        last[key] = x
      end
    end
  end
  ans == Float::INFINITY ? 0 : ans
end
