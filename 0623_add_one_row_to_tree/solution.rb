# LeetCode 0623 - Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} val
# @param {Integer} depth
# @return {TreeNode}
def add_one_row(root, val, depth)
  return TreeNode.new(val, root) if depth == 1

  dfs = lambda do |node, current|
    return if node.nil?

    if current == depth - 1
      node.left = TreeNode.new(val, node.left)
      node.right = TreeNode.new(val, nil, node.right)
      return
    end
    dfs.call(node.left, current + 1)
    dfs.call(node.right, current + 1)
  end

  dfs.call(root, 1)
  root
end
