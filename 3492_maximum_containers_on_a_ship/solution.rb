# LeetCode 3492 - Maximum Containers on a Ship
# https://leetcode.com/problems/maximum-containers-on-a-ship/

# @param {Integer} n
# @param {Integer} w
# @param {Integer} max_weight
# @return {Integer}
def max_containers(n, w, max_weight)
  cap = n * n
  by_w = max_weight / w
  cap < by_w ? cap : by_w
end
