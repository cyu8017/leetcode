# LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer[]} voyage
# @return {Integer[]}
def flip_match_voyage(root, voyage)
  i = [0]
  ans = []
  dfs = lambda do |node|
    return true if node.nil?
    return false if node.val != voyage[i[0]]

    i[0] += 1
    if node.left && node.left.val != voyage[i[0]]
      ans << node.val
      return dfs.call(node.right) && dfs.call(node.left)
    end
    dfs.call(node.left) && dfs.call(node.right)
  end
  dfs.call(root) ? ans : [-1]
end
