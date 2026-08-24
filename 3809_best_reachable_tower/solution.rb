# LeetCode 3809 - Best Reachable Tower
# https://leetcode.com/problems/best-reachable-tower/

# @param {Integer[][]} towers
# @param {Integer[]} center
# @param {Integer} radius
# @return {Integer[]}
def best_tower(towers, center, radius)
  cx, cy = center[0], center[1]
  idx = -1
  towers.each_with_index do |(x, y, q), i|
    dist = (x - cx).abs + (y - cy).abs
    next if dist > radius
    if idx == -1 || towers[idx][2] < q ||
       (towers[idx][2] == q &&
        (x < towers[idx][0] || (x == towers[idx][0] && y < towers[idx][1])))
      idx = i
    end
  end
  return [-1, -1] if idx == -1
  [towers[idx][0], towers[idx][1]]
end
