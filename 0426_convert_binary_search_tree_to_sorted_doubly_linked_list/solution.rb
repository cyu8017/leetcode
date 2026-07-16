# LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def tree_to_doubly_list(root)
    return nil if root.nil?

    state = { first: nil, last: nil }

    inorder = lambda do |node|
      return if node.nil?

      inorder.call(node.left)
      if state[:last]
        state[:last].right = node
        node.left = state[:last]
      else
        state[:first] = node
      end
      state[:last] = node
      inorder.call(node.right)
    end

    inorder.call(root)
    if state[:first] && state[:last]
      state[:first].left = state[:last]
      state[:last].right = state[:first]
    end
    state[:first]
  end

  alias_method :treeToDoublyList, :tree_to_doubly_list
end
