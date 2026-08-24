# LeetCode 0988 - Smallest String Starting From Leaf
# https://leetcode.com/problems/smallest-string-starting-from-leaf/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {String}
def smallest_from_leaf(root)
  best = "~"
  dfs = lambda do |node, path|
    return if node.nil?

    path = (97 + node.val).chr + path
    if node.left.nil? && node.right.nil?
      best = path if path < best
      return
    end
    dfs.call(node.left, path)
    dfs.call(node.right, path)
  end
  dfs.call(root, "")
  best
end
