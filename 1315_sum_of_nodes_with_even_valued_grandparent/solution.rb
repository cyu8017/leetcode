# LeetCode 1315 - Sum Of Nodes With Even Valued Grandparent
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

def sum_even_grandparent(root)
  dfs = lambda do |node, parent, grandparent|
    return 0 if node.nil?
    add = grandparent && grandparent.val.even? ? node.val : 0
    add + dfs.call(node.left, node, parent) + dfs.call(node.right, node, parent)
  end
  dfs.call(root, nil, nil)
end
