# LeetCode 0223 - Rectangle Area
# https://leetcode.com/problems/rectangle-area/

# @param {Integer} ax1
# @param {Integer} ay1
# @param {Integer} ax2
# @param {Integer} ay2
# @param {Integer} bx1
# @param {Integer} by1
# @param {Integer} bx2
# @param {Integer} by2
# @return {Integer}
def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
  area_a = (ax2 - ax1) * (ay2 - ay1)
  area_b = (bx2 - bx1) * (by2 - by1)
  overlap_w = [0, [ax2, bx2].min - [ax1, bx1].max].max
  overlap_h = [0, [ay2, by2].min - [ay1, by1].max].max
  area_a + area_b - overlap_w * overlap_h
end
