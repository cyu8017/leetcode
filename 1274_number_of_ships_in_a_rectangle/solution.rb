# LeetCode 1274 - Number of Ships in a Rectangle
# https://leetcode.com/problems/number-of-ships-in-a-rectangle/

# @param {Sea} sea
# @param {Integer[]} top_right
# @param {Integer[]} bottom_left
# @return {Integer}
def count_ships(sea, top_right, bottom_left)
  tx, ty = top_right
  bx, by = bottom_left
  return 0 if tx < bx || ty < by || !sea.hasShips(top_right, bottom_left)
  return 1 if tx == bx && ty == by
  mx = (tx + bx) / 2
  my = (ty + by) / 2
  count_ships(sea, [mx, my], [bx, by]) +
    count_ships(sea, [tx, my], [mx + 1, by]) +
    count_ships(sea, [mx, ty], [bx, my + 1]) +
    count_ships(sea, [tx, ty], [mx + 1, my + 1])
end
