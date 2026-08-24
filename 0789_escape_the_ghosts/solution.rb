# LeetCode 0789 - Escape The Ghosts
# https://leetcode.com/problems/escape-the-ghosts/

# @param {Integer[][]} ghosts
# @param {Integer[]} target
# @return {Boolean}
def escape_ghosts(ghosts, target)
  target_dist = target[0].abs + target[1].abs
  ghosts.all? { |gx, gy| (gx - target[0]).abs + (gy - target[1]).abs > target_dist }
end
