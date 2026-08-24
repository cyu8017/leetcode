# LeetCode 0987 - Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer[][]}
def vertical_traversal(root)
  nodes = []
  dfs = lambda do |node, row, col|
    return if node.nil?

    nodes << [col, row, node.val]
    dfs.call(node.left, row + 1, col - 1)
    dfs.call(node.right, row + 1, col + 1)
  end
  dfs.call(root, 0, 0)
  nodes.sort!
  ans = Hash.new { |h, k| h[k] = [] }
  nodes.each { |col, _, val| ans[col] << val }
  ans.keys.sort.map { |c| ans[c] }
end
