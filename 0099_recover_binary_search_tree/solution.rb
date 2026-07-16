# LeetCode 0099 - Recover Binary Search Tree
# https://leetcode.com/problems/recover-binary-search-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Void} Do not return anything, modify root in-place instead.
def recover_tree(root)
  first = nil
  second = nil
  previous = nil
  stack = []
  current = root

  while current || !stack.empty?
    while current
      stack << current
      current = current.left
    end
    current = stack.pop
    if previous && previous.val > current.val
      first = previous if first.nil?
      second = current
    end
    previous = current
    current = current.right
  end

  if first && second
    first.val, second.val = second.val, first.val
  end
end
