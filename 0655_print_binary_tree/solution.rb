# LeetCode 0655 - Print Binary Tree
# https://leetcode.com/problems/print-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {String[][]}
def print_tree(root)
  height = lambda do |node|
    return -1 if node.nil?

    1 + [height.call(node.left), height.call(node.right)].max
  end

  h = height.call(root)
  rows = h + 1
  cols = (1 << (h + 1)) - 1
  res = Array.new(rows) { Array.new(cols, "") }

  place = lambda do |node, r, c|
    return if node.nil?

    res[r][c] = node.val.to_s
    return if r == h

    offset = 1 << (h - r - 1)
    place.call(node.left, r + 1, c - offset)
    place.call(node.right, r + 1, c + offset)
  end

  place.call(root, 0, (cols - 1) / 2)
  res
end
