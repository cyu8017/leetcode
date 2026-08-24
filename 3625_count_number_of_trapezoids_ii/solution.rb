# LeetCode 3625 - Count Number of Trapezoids II
# https://leetcode.com/problems/count-number-of-trapezoids-ii/

# @param {Integer[][]} points
# @return {Integer}
def count_trapezoids(points)
  n = points.length
  cnt1 = {}
  cnt2 = {}
  get_or = lambda do |m, k|
    m[k] ||= {}
    m[k]
  end
  (0...n).each do |i|
    x1, y1 = points[i][0], points[i][1]
    (0...i).each do |j|
      x2, y2 = points[j][0], points[j][1]
      dx = x2 - x1
      dy = y2 - y1
      if dx == 0
        k = 1e9
        b = x1
      else
        k = dy.to_f / dx
        b = (y1 * dx - x1 * dy).to_f / dx
      end
      m1 = get_or.call(cnt1, k)
      m1[b] = (m1[b] || 0) + 1
      p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
      m2 = get_or.call(cnt2, p)
      m2[k] = (m2[k] || 0) + 1
    end
  end
  ans = 0
  cnt1.each_value do |e|
    s = 0
    e.each_value do |t|
      ans += s * t
      s += t
    end
  end
  cnt2.each_value do |e|
    s = 0
    e.each_value do |t|
      ans -= s * t
      s += t
    end
  end
  ans
end
