# LeetCode 0958 - Check Completeness of a Binary Tree
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Boolean}
def is_complete_tree(root)
  queue = [root]
  ended = false
  until queue.empty?
    node = queue.shift
    if node.nil?
      ended = true
    else
      return false if ended

      queue << node.left
      queue << node.right
    end
  end
  true
end
