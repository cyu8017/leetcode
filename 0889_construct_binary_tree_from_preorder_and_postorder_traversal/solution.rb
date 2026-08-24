# LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {Integer[]} preorder
# @param {Integer[]} postorder
# @return {TreeNode}
def construct_from_pre_post(preorder, postorder)
  post_index = {}
  postorder.each_with_index { |v, i| post_index[v] = i }

  build = lambda do |pre_lo, pre_hi, post_lo, post_hi|
    return nil if pre_lo > pre_hi

    root = TreeNode.new(preorder[pre_lo])
    return root if pre_lo == pre_hi

    left_val = preorder[pre_lo + 1]
    left_post = post_index[left_val]
    left_size = left_post - post_lo + 1
    root.left = build.call(pre_lo + 1, pre_lo + left_size, post_lo, left_post)
    root.right = build.call(pre_lo + left_size + 1, pre_hi, left_post + 1, post_hi - 1)
    root
  end

  n = preorder.length
  build.call(0, n - 1, 0, n - 1)
end
