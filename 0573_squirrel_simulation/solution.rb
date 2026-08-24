# LeetCode 0573 - Squirrel Simulation
# https://leetcode.com/problems/squirrel-simulation/

# @param {Integer} height
# @param {Integer} width
# @param {Integer[]} tree
# @param {Integer[]} squirrel
# @param {Integer[][]} nuts
# @return {Integer}
def min_distance(height, width, tree, squirrel, nuts)
  dist = lambda { |a, b| (a[0] - b[0]).abs + (a[1] - b[1]).abs }

  total = nuts.sum { |nut| 2 * dist.call(tree, nut) }
  best_save = nuts.map { |nut| dist.call(tree, nut) - dist.call(squirrel, nut) }.max
  total - best_save
end
