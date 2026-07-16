# LeetCode 0257 - Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {String[]}
def binary_tree_paths(root)
  result = []

  dfs = lambda do |node, path|
    return if node.nil?

    path << node.val.to_s
    if node.left.nil? && node.right.nil?
      result << path.join('->')
    else
      dfs.call(node.left, path)
      dfs.call(node.right, path)
    end
    path.pop
  end

  dfs.call(root, [])
  result
end
