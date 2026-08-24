# LeetCode 2641 - Cousins in Binary Tree II
# https://leetcode.com/problems/cousins-in-binary-tree-ii/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {TreeNode}
def replace_value_in_tree(root)
  return nil if root.nil?

  root.val = 0
  q = [root]
  until q.empty?
    sz = q.length
    level_sum = 0
    level = []
    sz.times do
      node = q.shift
      level << node
      level_sum += node.left.val if node.left
      level_sum += node.right.val if node.right
    end
    level.each do |node|
      cousin = level_sum
      cousin -= node.left.val if node.left
      cousin -= node.right.val if node.right
      if node.left
        node.left.val = cousin
        q << node.left
      end
      if node.right
        node.right.val = cousin
        q << node.right
      end
    end
  end
  root
end
