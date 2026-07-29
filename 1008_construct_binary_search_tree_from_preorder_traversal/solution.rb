# LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {Integer[]} preorder
# @return {TreeNode}
def bst_from_preorder(preorder)
  i = 0
  build = lambda do |bound|
    return nil if i == preorder.length || preorder[i] > bound

    root = TreeNode.new(preorder[i])
    i += 1
    root.left = build.call(root.val)
    root.right = build.call(bound)
    root
  end
  build.call(Float::INFINITY)
end
