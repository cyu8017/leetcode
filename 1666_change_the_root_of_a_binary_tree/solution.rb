# LeetCode 1666 - Change the Root of a Binary Tree
# https://leetcode.com/problems/change-the-root-of-a-binary-tree/

# @param {TreeNode} root
# @param {TreeNode} leaf
# @return {TreeNode}
def flip_binary_tree(root, leaf)
  node = leaf
  while node != root
    parent = node.parent
    if parent.left.equal?(node)
      parent.left = nil
    else
      parent.right = nil
    end
    original_left = node.left
    node.left = parent
    node.right = original_left unless original_left.nil?
    node = parent
  end
  fix_parent = lambda do |cur, parent|
    return if cur.nil?

    cur.parent = parent
    fix_parent.call(cur.left, cur)
    fix_parent.call(cur.right, cur)
  end
  fix_parent.call(leaf, nil)
  leaf
end
