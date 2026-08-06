# LeetCode 1924 - Erect the Fence II
# https://leetcode.com/problems/erect-the-fence-ii/

# @param {Integer[][]} trees
# @return {Float[]}
def outer_trees(trees)
  pts = trees.map { |p| [p[0].to_f, p[1].to_f] }
  (pts.length - 1).downto(1) do |i|
    j = rand(i + 1)
    pts[i], pts[j] = pts[j], pts[i]
  end

  dist = ->(a, b) { Math.hypot(a[0] - b[0], a[1] - b[1]) }
  circle2 = lambda do |a, b|
    c = [(a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0]
    [c, dist.call(a, b) / 2.0]
  end
  circle3 = lambda do |a, b, c|
    ax, ay = a
    bx, by = b
    cx, cy = c
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if d.abs < 1e-12
      return [circle2.call(a, b), circle2.call(a, c), circle2.call(b, c)].min_by { |x| x[1] }
    end
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    center = [ux, uy]
    [center, dist.call(center, a)]
  end
  inside = ->(cir, p) { cir && dist.call(cir[0], p) <= cir[1] + 1e-9 }

  circle = nil
  pts.each_with_index do |p, i|
    next if circle && inside.call(circle, p)
    circle = [p, 0.0]
    i.times do |j|
      q = pts[j]
      next if inside.call(circle, q)
      circle = circle2.call(p, q)
      j.times do |k|
        r = pts[k]
        circle = circle3.call(p, q, r) unless inside.call(circle, r)
      end
    end
  end
  [circle[0][0], circle[0][1], circle[1]]
end
