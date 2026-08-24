# LeetCode 0993 - Cousins in Binary Tree
# https://leetcode.com/problems/cousins-in-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} x
# @param {Integer} y
# @return {Boolean}
def is_cousins(root, x, y)
  info = {}
  dfs = lambda do |node, parent, depth|
    return if node.nil?

    info[node.val] = [depth, parent] if node.val == x || node.val == y
    dfs.call(node.left, node, depth + 1)
    dfs.call(node.right, node, depth + 1)
  end
  dfs.call(root, nil, 0)
  info[x][0] == info[y][0] && !info[x][1].equal?(info[y][1])
end
