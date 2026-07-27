# LeetCode 1620 - Coordinate With Maximum Network Quality
# https://leetcode.com/problems/coordinate-with-maximum-network-quality/

# @param {Integer[][]} towers
# @param {Integer} radius
# @return {Integer[]}
def best_coordinate(towers, radius)
  best = [0, 0]
  quality = -1
  (0..50).each do |x|
    (0..50).each do |y|
      q = 0
      towers.each do |a, b, v|
        d = Math.hypot(x - a, y - b)
        q += (v / (1 + d)).to_i if d <= radius
      end
      if q > quality
        quality = q
        best = [x, y]
      end
    end
  end
  best
end
