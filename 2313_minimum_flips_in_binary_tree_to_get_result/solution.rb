# LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
# https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Boolean} result
# @return {Integer}
def minimum_flips(root, result)
  dfs = lambda do |node|
    if node.left.nil? && node.right.nil?
      return node.val == 0 ? [0, 1] : [1, 0]
    end
    if node.val == 5
      x = dfs.call(node.left)
      return [x[1], x[0]]
    end
    l = dfs.call(node.left)
    r = dfs.call(node.right)
    lf, lt, rf, rt = l[0], l[1], r[0], r[1]
    return [lf + rf, [lt + rt, lt + rf, lf + rt].min] if node.val == 2
    return [[lf + rf, lf + rt, lt + rf].min, lt + rt] if node.val == 3
    return [[lf + rf, lt + rt].min, [lf + rt, lt + rf].min] if node.val == 4
    [0, 0]
  end
  res = dfs.call(root)
  result ? res[1] : res[0]
end

alias solve minimum_flips
