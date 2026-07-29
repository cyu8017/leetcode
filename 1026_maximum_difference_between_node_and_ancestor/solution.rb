# LeetCode 1026 - Maximum Difference Between Node and Ancestor
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# @param {TreeNode} root
# @return {Integer}
def max_ancestor_diff(root)
  dfs = lambda do |node, lo, hi|
    return hi - lo if node.nil?

    lo = [lo, node.val].min
    hi = [hi, node.val].max
    [dfs.call(node.left, lo, hi), dfs.call(node.right, lo, hi)].max
  end
  dfs.call(root, root.val, root.val)
end
