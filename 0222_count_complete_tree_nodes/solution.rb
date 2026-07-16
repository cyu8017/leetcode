# LeetCode 0222 - Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

def left_depth(node)
  depth = 0
  while node
    depth += 1
    node = node.left
  end
  depth
end

def right_depth(node)
  depth = 0
  while node
    depth += 1
    node = node.right
  end
  depth
end

# @param {TreeNode} root
# @return {Integer}
def count_nodes(root)
  return 0 if root.nil?

  left = left_depth(root)
  right = right_depth(root)
  return (1 << left) - 1 if left == right

  1 + count_nodes(root.left) + count_nodes(root.right)
end
