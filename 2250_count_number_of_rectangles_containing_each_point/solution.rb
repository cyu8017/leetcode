# LeetCode 2250 - Count Number of Rectangles Containing Each Point
# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

# @param {Integer[][]} rectangles
# @param {Integer[][]} points
# @return {Integer[]}
def count_rectangles(rectangles, points)
  by_h = Array.new(101) { [] }
  rectangles.each { |x, h| by_h[h] << x }
  (1..100).each { |h| by_h[h].sort! }
  ans = Array.new(points.length, 0)
  points.each_with_index do |(x, y), i|
    cnt = 0
    (y..100).each do |h|
      xs = by_h[h]
      lo = 0
      hi = xs.length
      while lo < hi
        mid = (lo + hi) >> 1
        if xs[mid] < x
          lo = mid + 1
        else
          hi = mid
        end
      end
      cnt += xs.length - lo
    end
    ans[i] = cnt
  end
  ans
end
