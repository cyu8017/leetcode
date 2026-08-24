# LeetCode 2013 - Detect Squares
# https://leetcode.com/problems/detect-squares/

class DetectSquares
  def initialize
    @cnt = Hash.new(0)
  end

  def add(point)
    @cnt[key(point[0], point[1])] += 1
    nil
  end

  def count(point)
    x = point[0]
    y = point[1]
    ans = 0
    @cnt.each do |k, c|
      px, py = k.split(",").map(&:to_i)
      next if px == x || py == y
      next if (px - x).abs != (py - y).abs

      ans += c * @cnt[key(px, y)] * @cnt[key(x, py)]
    end
    ans
  end

  private

  def key(x, y)
    "#{x},#{y}"
  end
end
