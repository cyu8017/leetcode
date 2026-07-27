# LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

# @param {TreeNode} root
# @param {TreeNode[]} nodes
# @return {TreeNode}
def lowest_common_ancestor(root, nodes)
  targets = {}
  nodes.each do |node|
    if node.respond_to?(:val)
      targets[node.object_id] = true
    else
      targets[node] = true
    end
  end
  match = lambda do |node|
    return false if node.nil?

    targets[node.object_id] || targets[node.val]
  end
  dfs = lambda do |node|
    return nil if node.nil?

    l = dfs.call(node.left)
    r = dfs.call(node.right)
    return node if match.call(node) || (l && r)

    l || r
  end
  dfs.call(root)
end
