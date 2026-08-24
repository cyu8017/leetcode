# LeetCode 2543 - Check if Point Is Reachable
# https://leetcode.com/problems/check-if-point-is-reachable/

# @param {Integer} target_x
# @param {Integer} target_y
# @return {Boolean}
def is_reachable(target_x, target_y)
  g = target_x.gcd(target_y)
  g /= 2 while g.even?
  g == 1
end
