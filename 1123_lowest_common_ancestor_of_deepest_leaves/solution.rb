# LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# @param {TreeNode} root
# @return {TreeNode}
def lca_deepest_leaves(root)
  dfs = nil
  dfs = lambda do |node|
    return [nil, 0] if node.nil?
    left_node, left_d = dfs.call(node.left)
    right_node, right_d = dfs.call(node.right)
    if left_d > right_d
      [left_node, left_d + 1]
    elsif right_d > left_d
      [right_node, right_d + 1]
    else
      [node, left_d + 1]
    end
  end
  dfs.call(root)[0]
end
