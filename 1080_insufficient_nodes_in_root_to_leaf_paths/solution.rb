# LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left, @right = left, right
#     end
# end
# @param {TreeNode} root
# @param {Integer} limit
# @return {TreeNode}
def sufficient_subset(root, limit)
  dfs = lambda do |node, path_sum|
    return nil if node.nil?

    path_sum += node.val
    if node.left.nil? && node.right.nil?
      return path_sum >= limit ? node : nil
    end

    node.left = dfs.call(node.left, path_sum)
    node.right = dfs.call(node.right, path_sum)
    return nil if node.left.nil? && node.right.nil?

    node
  end

  dfs.call(root, 0)
end
