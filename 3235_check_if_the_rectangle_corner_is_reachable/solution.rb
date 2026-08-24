# LeetCode 3235 - Check if the Rectangle Corner Is Reachable
# https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

# @param {Integer} x_corner
# @param {Integer} y_corner
# @param {Integer[][]} circles
# @return {Boolean}
def can_reach_corner(x_corner, y_corner, circles)
  n = circles.length
  vis = Array.new(n, false)
  in_circle = lambda do |x, y, cx, cy, r|
    dx = x - cx
    dy = y - cy
    dx * dx + dy * dy <= r * r
  end
  cross_left_top = lambda do |cx, cy, r|
    a = cx.abs <= r && cy >= 0 && cy <= y_corner
    b = (cy - y_corner).abs <= r && cx >= 0 && cx <= x_corner
    a || b
  end
  cross_right_bottom = lambda do |cx, cy, r|
    a = (cx - x_corner).abs <= r && cy >= 0 && cy <= y_corner
    b = cy.abs <= r && cx >= 0 && cx <= x_corner
    a || b
  end
  dfs = nil
  dfs = lambda do |i|
    x1, y1, r1 = circles[i]
    return true if cross_right_bottom.call(x1, y1, r1)
    vis[i] = true
    (0...n).each do |j|
      next if vis[j]
      x2, y2, r2 = circles[j]
      next if (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) > (r1 + r2) * (r1 + r2)
      if x1 * r2 + x2 * r1 < (r1 + r2) * x_corner && y1 * r2 + y2 * r1 < (r1 + r2) * y_corner && dfs.call(j)
        return true
      end
    end
    false
  end
  (0...n).each do |i|
    x, y, r = circles[i]
    return false if in_circle.call(0, 0, x, y, r) || in_circle.call(x_corner, y_corner, x, y, r)
    return false if !vis[i] && cross_left_top.call(x, y, r) && dfs.call(i)
  end
  true
end
