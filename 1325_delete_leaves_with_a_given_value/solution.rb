# LeetCode 1325 - Delete Leaves With A Given Value
# https://leetcode.com/problems/delete-leaves-with-a-given-value/

def remove_leaf_nodes(root, target)
  return nil if root.nil?
  root.left = remove_leaf_nodes(root.left, target)
  root.right = remove_leaf_nodes(root.right, target)
  return nil if root.left.nil? && root.right.nil? && root.val == target
  root
end
