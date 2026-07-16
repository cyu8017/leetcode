# LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {Integer[]} inorder
# @param {Integer[]} postorder
# @return {TreeNode}
def build_tree(inorder, postorder)
  index = {}
  inorder.each_with_index { |v, i| index[v] = i }
  post_index = [postorder.length - 1]

  build = lambda do |left, right|
    return nil if left > right

    root_val = postorder[post_index[0]]
    post_index[0] -= 1
    mid = index[root_val]
    root = TreeNode.new(root_val)
    root.right = build.call(mid + 1, right)
    root.left = build.call(left, mid - 1)
    root
  end

  build.call(0, inorder.length - 1)
end