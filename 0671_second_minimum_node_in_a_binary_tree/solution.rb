# LeetCode 0671 - Second Minimum Node In a Binary Tree
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

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
def find_second_minimum_value(root)
  return -1 if root.nil?

  ans = -1
  dfs = lambda do |node|
    return if node.nil?

    if node.val > root.val
      ans = node.val if ans == -1 || node.val < ans
      return
    end
    dfs.call(node.left)
    dfs.call(node.right)
  end

  dfs.call(root)
  ans
end
