# LeetCode 1120 - Maximum Average Subtree
# https://leetcode.com/problems/maximum-average-subtree/

# @param {TreeNode} root
# @return {Float}
def maximum_average_subtree(root)
  best = 0.0
  dfs = nil
  dfs = lambda do |node|
    return [0, 0] if node.nil?
    ls, lc = dfs.call(node.left)
    rs, rc = dfs.call(node.right)
    s = ls + rs + node.val
    c = lc + rc + 1
    best = [best, s.to_f / c].max
    [s, c]
  end
  dfs.call(root)
  best
end
