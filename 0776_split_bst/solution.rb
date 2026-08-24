# LeetCode 0776 - Split BST
# https://leetcode.com/problems/split-bst/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} target
# @return {TreeNode[]}
def split_bst(root, target)
  split = lambda do |node|
    return [nil, nil] if node.nil?

    if node.val <= target
      left, right = split.call(node.right)
      node.right = left
      [node, right]
    else
      left, right = split.call(node.left)
      node.left = right
      [left, node]
    end
  end

  tree_to_arr = lambda do |node|
    return [] if node.nil?

    values = []
    queue = [node]
    until queue.empty?
      cur = queue.shift
      if cur.nil?
        values << nil
        next
      end
      values << cur.val
      queue << cur.left
      queue << cur.right
    end
    values.pop while !values.empty? && values.last.nil?
    values
  end

  left, right = split.call(root)
  [tree_to_arr.call(left), tree_to_arr.call(right)]
end
