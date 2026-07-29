# LeetCode 1022 - Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# @param {TreeNode} root
# @return {Integer}
def sum_root_to_leaf(root)
  dfs = lambda do |node, value|
    return 0 if node.nil?

    value = value * 2 + node.val
    return value if node.left.nil? && node.right.nil?

    dfs.call(node.left, value) + dfs.call(node.right, value)
  end
  dfs.call(root, 0)
end
