# LeetCode 1453 - Maximum Number Of Darts Inside Of A Circular Dartboard
# https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

def num_points(darts, r)
  ans = darts.empty? ? 0 : 1
  darts.each_with_index do |(x1, y1), i|
    darts[(i + 1)..].each do |x2, y2|
      dx = x2 - x1
      dy = y2 - y1
      d2 = dx * dx + dy * dy
      next if d2 > 4 * r * r || d2 == 0
      d = Math.sqrt(d2)
      h = Math.sqrt(r * r - d2 / 4.0)
      mx = (x1 + x2) / 2.0
      my = (y1 + y2) / 2.0
      [-1, 1].each do |sign|
        cx = mx + sign * (-dy) * h / d
        cy = my + sign * dx * h / d
        count = darts.count { |x, y| (x - cx) ** 2 + (y - cy) ** 2 <= r * r + 1e-7 }
        ans = [ans, count].max
      end
    end
  end
  ans
end
