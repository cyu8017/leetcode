# LeetCode 1448 - Count Good Nodes In Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

def good_nodes(root)
  visit = lambda do |node, maximum|
    return 0 if node.nil?
    good = node.val >= maximum ? 1 : 0
    maximum = [maximum, node.val].max
    good + visit.call(node.left, maximum) + visit.call(node.right, maximum)
  end
  visit.call(root, -Float::INFINITY)
end
