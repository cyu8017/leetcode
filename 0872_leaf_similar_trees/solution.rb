# LeetCode 0872 - Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root1
# @param {TreeNode} root2
# @return {Boolean}
def leaf_similar(root1, root2)
  leaves = lambda do |node|
    return [] if node.nil?
    return [node.val] if node.left.nil? && node.right.nil?

    leaves.call(node.left) + leaves.call(node.right)
  end

  leaves.call(root1) == leaves.call(root2)
end
