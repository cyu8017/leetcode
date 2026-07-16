# LeetCode 0235 - Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)
  current = root
  while current
    if p.val < current.val && q.val < current.val
      current = current.left
    elsif p.val > current.val && q.val > current.val
      current = current.right
    else
      return current
    end
  end
  current
end
