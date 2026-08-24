# LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} fx
# @param {Integer} fy
# @param {Integer} t
# @return {Boolean}
def is_reachable_at_time(sx, sy, fx, fy, t)
  need = [(sx - fx).abs, (sy - fy).abs].max
  return t != 1 if need == 0

  t >= need
end
