# LeetCode 1932 - Merge BSTs to Create Single BST
# https://leetcode.com/problems/merge-bsts-to-create-single-bst/

# @param {TreeNode[]} trees
# @return {TreeNode}
def can_merge(trees)
  value_to_root = {}
  count = Hash.new(0)
  trees.each do |tree|
    value_to_root[tree.val] = tree
    count[tree.val] += 1
    count[tree.left.val] += 1 if tree.left
    count[tree.right.val] += 1 if tree.right
  end
  roots = trees.select { |t| count[t.val] == 1 }
  return nil unless roots.length == 1
  root = roots[0]

  merge = lambda do |node|
    return true unless node
    if node.left && value_to_root.key?(node.left.val)
      node.left = value_to_root[node.left.val]
      value_to_root.delete(node.left.val)
    end
    if node.right && value_to_root.key?(node.right.val)
      node.right = value_to_root[node.right.val]
      value_to_root.delete(node.right.val)
    end
    merge.call(node.left) && merge.call(node.right)
  end

  value_to_root.delete(root.val)
  return nil if !merge.call(root) || !value_to_root.empty?

  is_valid_bst = lambda do |node, lo, hi|
    return true unless node
    return false unless lo < node.val && node.val < hi
    is_valid_bst.call(node.left, lo, node.val) && is_valid_bst.call(node.right, node.val, hi)
  end

  is_valid_bst.call(root, -Float::INFINITY, Float::INFINITY) ? root : nil
end
