# LeetCode 2773 - Height of Special Binary Tree
# https://leetcode.com/problems/height-of-special-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer}
def height_of_tree(root)
  return -1 if root.nil?

  dfs = lambda do |node|
    return -1 if node.nil?
    return dfs.call(node.right) + 1 if node.left && node.left.right.equal?(node)
    return dfs.call(node.left) + 1 if node.right && node.right.left.equal?(node)
    [dfs.call(node.left), dfs.call(node.right)].max + 1
  end
  dfs.call(root)
end
