# LeetCode 0270 - Closest Binary Search Tree Value
# https://leetcode.com/problems/closest-binary-search-tree-value/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Float} target
# @return {Integer}
def closest_value(root, target)
  closest = root.val
  current = root
  while current
    closest = current.val if (closest - target).abs > (current.val - target).abs
    return current.val if current.val == target

    current = target < current.val ? current.left : current.right
  end
  closest
end
