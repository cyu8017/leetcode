# LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

def _same_node_1644(a, b)
  return false if a.nil? || b.nil?
  return true if a.equal?(b)

  av = a.respond_to?(:val) ? a.val : a
  bv = b.respond_to?(:val) ? b.val : b
  av == bv
end

# @param {TreeNode} root
# @param {TreeNode|Integer} p
# @param {TreeNode|Integer} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)
  found = 0
  dfs = lambda do |node|
    return nil if node.nil?

    left = dfs.call(node.left)
    right = dfs.call(node.right)
    if _same_node_1644(node, p) || _same_node_1644(node, q)
      found += 1
      return node
    end
    left && right ? node : (left || right)
  end
  ans = dfs.call(root)
  found == 2 ? ans : nil
end
