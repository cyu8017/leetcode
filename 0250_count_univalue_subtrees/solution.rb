# LeetCode 0250 - Count Univalue Subtrees
# https://leetcode.com/problems/count-univalue-subtrees/

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
def count_univalue_subtrees(root)
  count = 0

  dfs = lambda do |node|
    return true if node.nil?

    left_ok = dfs.call(node.left)
    right_ok = dfs.call(node.right)
    return false unless left_ok && right_ok
    return false if node.left && node.left.val != node.val
    return false if node.right && node.right.val != node.val

    count += 1
    true
  end

  dfs.call(root)
  count
end
