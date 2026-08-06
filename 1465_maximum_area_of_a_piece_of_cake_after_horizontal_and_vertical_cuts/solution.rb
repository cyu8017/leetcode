# LeetCode 1465 - Maximum Area Of A Piece Of Cake After Horizontal And Vertical Cuts
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

def max_area(h, w, horizontal_cuts, vertical_cuts)
  hs = ([0, h] + horizontal_cuts).sort
  vs = ([0, w] + vertical_cuts).sort
  max_h = hs.each_cons(2).map { |a, b| b - a }.max
  max_v = vs.each_cons(2).map { |a, b| b - a }.max
  max_h * max_v % 1_000_000_007
end
