# LeetCode 1457 - Pseudo Palindromic Paths In A Binary Tree
# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

def pseudo_palindromic_paths(root)
  dfs = lambda do |node, mask|
    return 0 if node.nil?
    mask ^= 1 << node.val
    if node.left.nil? && node.right.nil?
      return (mask & (mask - 1)) == 0 ? 1 : 0
    end
    dfs.call(node.left, mask) + dfs.call(node.right, mask)
  end
  dfs.call(root, 0)
end
