# LeetCode 1028 - Recover a Tree From Preorder Traversal
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {String} traversal
# @return {TreeNode}
def recover_from_preorder(traversal)
  stack = []
  i = 0
  n = traversal.length
  while i < n
    depth = 0
    while i < n && traversal[i] == "-"
      depth += 1
      i += 1
    end
    start = i
    while i < n && traversal[i].match?(/\d/)
      i += 1
    end
    node = TreeNode.new(traversal[start...i].to_i)
    stack.pop while stack.length > depth
    unless stack.empty?
      if stack[-1].left.nil?
        stack[-1].left = node
      else
        stack[-1].right = node
      end
    end
    stack << node
  end
  stack[0]
end
