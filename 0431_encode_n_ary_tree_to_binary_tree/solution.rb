# LeetCode 0431 - Encode N-ary Tree to Binary Tree
# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

class Node
  attr_accessor :val, :children

  def initialize(val = nil, children = nil)
    @val = val
    @children = children || []
  end
end

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def encode_nary_tree(root)
    return nil if root.nil?

    binary = TreeNode.new(root.val)
    return binary if root.children.empty?

    binary.left = encode_nary_tree(root.children[0])
    sibling = binary.left
    root.children[1..].each do |child|
      sibling.right = encode_nary_tree(child)
      sibling = sibling.right
    end
    binary
  end

  def decode_binary_tree(root)
    return nil if root.nil?

    node = Node.new(root.val, [])
    current = root.left
    while current
      node.children << decode_binary_tree(current)
      current = current.right
    end
    node
  end

  alias_method :encodeNaryTree, :encode_nary_tree
  alias_method :decodeBinaryTree, :decode_binary_tree
end
