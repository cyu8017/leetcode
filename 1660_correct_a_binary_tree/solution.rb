# LeetCode 1660 - Correct a Binary Tree
# https://leetcode.com/problems/correct-a-binary-tree/

# @param {TreeNode} root
# @return {TreeNode}
def correct_binary_tree(root)
  seen = {}
  dfs = lambda do |node|
    return nil if node.nil?
    return nil if node.right && seen[node.right.object_id]

    seen[node.object_id] = true
    node.right = dfs.call(node.right)
    node.left = dfs.call(node.left)
    node
  end
  dfs.call(root)
end
