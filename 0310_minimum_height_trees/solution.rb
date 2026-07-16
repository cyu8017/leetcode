# LeetCode 0310 - Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/

class Solution
  def findMinHeightTrees(n, edges)
    return (0...n).to_a if n <= 2

    graph = Array.new(n) { [] }
    degree = Array.new(n, 0)
    edges.each do |left, right|
      graph[left] << right
      graph[right] << left
      degree[left] += 1
      degree[right] += 1
    end

    leaves = (0...n).select { |node| degree[node] == 1 }
    remaining = n
    while remaining > 2
      remaining -= leaves.length
      new_leaves = []
      leaves.each do |leaf|
        graph[leaf].each do |neighbor|
          degree[neighbor] -= 1
          new_leaves << neighbor if degree[neighbor] == 1
        end
      end
      leaves = new_leaves
    end
    leaves
  end
end
