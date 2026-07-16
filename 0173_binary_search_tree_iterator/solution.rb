# LeetCode 0173 - Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class BSTIterator
  def initialize(root)
    @stack = []
    push_left(root)
  end

  def next
    node = @stack.pop
    push_left(node.right)
    node.val
  end

  def has_next
    !@stack.empty?
  end

  private

  def push_left(node)
    while node
      @stack << node
      node = node.left
    end
  end
end