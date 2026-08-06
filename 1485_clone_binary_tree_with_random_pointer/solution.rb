# LeetCode 1485 - Clone Binary Tree With Random Pointer
# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

class Node
  attr_accessor :val, :left, :right, :random

  def initialize(val = 0)
    @val = val
    @left = nil
    @right = nil
    @random = nil
  end
end

def copy_random_binary_tree(root)
  copies = {}
  clone = lambda do |node|
    return nil if node.nil?
    unless copies.key?(node)
      copies[node] = Node.new(node.val)
      copies[node].left = clone.call(node.left)
      copies[node].right = clone.call(node.right)
      copies[node].random = clone.call(node.random)
    end
    copies[node]
  end
  clone.call(root)
end
