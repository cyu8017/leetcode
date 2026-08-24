# LeetCode 0973 - K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

# @param {Integer[][]} points
# @param {Integer} k
# @return {Integer[][]}
def k_closest(points, k)
  points.sort_by { |p| p[0] * p[0] + p[1] * p[1] }[0, k]
end
