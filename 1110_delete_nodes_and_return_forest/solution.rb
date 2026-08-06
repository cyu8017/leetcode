# LeetCode 1110 - Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest/

require "set"

# @param {TreeNode} root
# @param {Integer[]} to_delete
# @return {TreeNode[]}
def del_nodes(root, to_delete)
  delete = Set.new(to_delete)
  forest = []
  dfs = nil
  dfs = lambda do |node, is_root|
    return nil if node.nil?
    removed = delete.include?(node.val)
    forest << node if is_root && !removed
    node.left = dfs.call(node.left, removed)
    node.right = dfs.call(node.right, removed)
    removed ? nil : node
  end
  dfs.call(root, true)
  forest
end
