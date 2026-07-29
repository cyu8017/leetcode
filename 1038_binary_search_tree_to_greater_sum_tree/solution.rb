# LeetCode 1038 - Binary Search Tree to Greater Sum Tree
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# @param {TreeNode} root
# @return {TreeNode}
def bst_to_gst(root)
  total = 0
  reverse_inorder = lambda do |node|
    return if node.nil?

    reverse_inorder.call(node.right)
    total += node.val
    node.val = total
    reverse_inorder.call(node.left)
  end
  reverse_inorder.call(root)
  root
end
