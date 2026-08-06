# LeetCode 1373 - Maximum Sum Bst In Binary Tree
# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

def max_sum_bst(root)
  ans = 0
  dfs = lambda do |node|
    return [true, Float::INFINITY, -Float::INFINITY, 0] if node.nil?
    a, lx, lh, ls = dfs.call(node.left)
    b, rx, rh, rs = dfs.call(node.right)
    if a && b && lh < node.val && node.val < rx
      s = ls + rs + node.val
      ans = [ans, s].max
      return [true, [lx, node.val].min, [rh, node.val].max, s]
    end
    [false, 0, 0, 0]
  end
  dfs.call(root)
  ans
end
