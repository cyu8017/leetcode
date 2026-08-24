# LeetCode 0897 - Increasing Order Search Tree
# https://leetcode.com/problems/increasing-order-search-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {TreeNode}
def increasing_bst(root)
  dummy = TreeNode.new(0)
  cur = [dummy]
  inorder = lambda do |node|
    return if node.nil?

    inorder.call(node.left)
    node.left = nil
    cur[0].right = node
    cur[0] = node
    inorder.call(node.right)
  end
  inorder.call(root)
  dummy.right
end
