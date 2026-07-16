# LeetCode 0230 - Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def kth_smallest(root, k)
  stack = []
  current = root

  while current || !stack.empty?
    while current
      stack << current
      current = current.left
    end
    current = stack.pop
    k -= 1
    return current.val if k.zero?
    current = current.right
  end

  -1
end
