# LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

# @param {Integer[][]} bottom_left
# @param {Integer[][]} top_right
# @return {Integer}
def largest_square_area(bottom_left, top_right)
  return 0 if bottom_left.nil? || top_right.nil?

  ans = 0
  n = bottom_left.length
  n.times do |i|
    x1 = bottom_left[i][0]
    y1 = bottom_left[i][1]
    x2 = top_right[i][0]
    y2 = top_right[i][1]
    (i + 1...n).each do |j|
      x3 = bottom_left[j][0]
      y3 = bottom_left[j][1]
      x4 = top_right[j][0]
      y4 = top_right[j][1]
      ww = [x2, x4].min - [x1, x3].max
      h = [y2, y4].min - [y1, y3].max
      e = [ww, h].min
      ans = e * e if e > 0 && e * e > ans
    end
  end
  ans
end
