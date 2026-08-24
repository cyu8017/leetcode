# LeetCode 0701 - Insert into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/

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
# @return {TreeNode}
def insert_into_bst(root, val)
  return TreeNode.new(val) if root.nil?

  node = root
  loop do
    if val < node.val
      if node.left.nil?
        node.left = TreeNode.new(val)
        break
      end
      node = node.left
    else
      if node.right.nil?
        node.right = TreeNode.new(val)
        break
      end
      node = node.right
    end
  end
  root
end
