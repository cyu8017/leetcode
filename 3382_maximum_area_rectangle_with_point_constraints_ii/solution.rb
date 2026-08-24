# LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def pack_point(x, y)
  (x << 32) ^ (y & 0xFFFFFFFF)
end

# @param {Integer[]} x_coord
# @param {Integer[]} y_coord
# @return {Integer}
def max_rectangle_area(x_coord, y_coord)
  n = x_coord.length
  points = n.times.map { |i| [x_coord[i], y_coord[i]] }
  s = {}
  points.each { |p| s[pack_point(p[0], p[1])] = true }
  ans = -1
  n.times do |i|
    ((i + 1)...n).each do |j|
      x1 = points[i][0]
      y1 = points[i][1]
      x2 = points[j][0]
      y2 = points[j][1]
      next if x1 == x2 || y1 == y2
      next unless s[pack_point(x1, y2)] && s[pack_point(x2, y1)]

      min_x = [x1, x2].min
      max_x = [x1, x2].max
      min_y = [y1, y2].min
      max_y = [y1, y2].max
      good = true
      points.each do |p|
        x = p[0]
        y = p[1]
        if x > min_x && x < max_x && y > min_y && y < max_y
          good = false
          break
        end
        on_border = ((x == min_x || x == max_x) && y >= min_y && y <= max_y) ||
                    ((y == min_y || y == max_y) && x >= min_x && x <= max_x)
        next unless on_border

        is_corner = (x == min_x || x == max_x) && (y == min_y || y == max_y)
        unless is_corner
          good = false
          break
        end
      end
      if good
        area = (max_x - min_x) * (max_y - min_y)
        ans = area if area > ans
      end
    end
  end
  ans
end
