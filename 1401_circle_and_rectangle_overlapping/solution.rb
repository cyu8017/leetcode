# LeetCode 1401 - Circle And Rectangle Overlapping
# https://leetcode.com/problems/circle-and-rectangle-overlapping/

def check_overlap(radius, x_center, y_center, x1, y1, x2, y2)
  x = [[x_center, x1].max, x2].min
  y = [[y_center, y1].max, y2].min
  (x - x_center) ** 2 + (y - y_center) ** 2 <= radius ** 2
end
