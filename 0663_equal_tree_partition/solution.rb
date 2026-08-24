# LeetCode 0663 - Equal Tree Partition
# https://leetcode.com/problems/equal-tree-partition/

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
def check_equal_tree(root)
  subtree_sums = []

  dfs = lambda do |node|
    return 0 if node.nil?

    total = node.val + dfs.call(node.left) + dfs.call(node.right)
    subtree_sums << total
    total
  end

  total = dfs.call(root)
  subtree_sums.pop
  total.even? && subtree_sums.include?(total / 2)
end
