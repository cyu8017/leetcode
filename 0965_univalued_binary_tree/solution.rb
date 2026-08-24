# LeetCode 0965 - Univalued Binary Tree
# https://leetcode.com/problems/univalued-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Boolean}
def is_unival_tree(root)
  return true if root.nil?

  dfs = lambda do |node|
    return true if node.nil?
    return false if node.val != root.val

    dfs.call(node.left) && dfs.call(node.right)
  end
  dfs.call(root)
end
