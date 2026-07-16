# LeetCode 0129 - Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

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
def sum_numbers(root)
  dfs = lambda do |node, value|
    next 0 if node.nil?

    current = value * 10 + node.val
    next current if node.left.nil? && node.right.nil?

    dfs.call(node.left, current) + dfs.call(node.right, current)
  end
  dfs.call(root, 0)
end