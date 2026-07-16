# LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {Integer[]} preorder
# @param {Integer[]} inorder
# @return {TreeNode}
def build_tree(preorder, inorder)
  index = {}
  inorder.each_with_index { |v, i| index[v] = i }
  pre_index = [0]

  build = lambda do |left, right|
    return nil if left > right

    root_val = preorder[pre_index[0]]
    pre_index[0] += 1
    mid = index[root_val]
    root = TreeNode.new(root_val)
    root.left = build.call(left, mid - 1)
    root.right = build.call(mid + 1, right)
    root
  end

  build.call(0, inorder.length - 1)
end