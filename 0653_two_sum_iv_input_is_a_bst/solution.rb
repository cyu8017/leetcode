# LeetCode 0653 - Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} k
# @return {Boolean}
def find_target(root, k)
  seen = {}

  dfs = lambda do |node|
    return false if node.nil?
    return true if seen.key?(k - node.val)

    seen[node.val] = true
    dfs.call(node.left) || dfs.call(node.right)
  end

  dfs.call(root)
end
