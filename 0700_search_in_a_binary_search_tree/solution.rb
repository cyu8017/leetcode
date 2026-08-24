# LeetCode 0700 - Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} val
# @return {TreeNode}
def search_bst(root, val)
  while root && root.val != val
    root = val < root.val ? root.left : root.right
  end
  root
end
