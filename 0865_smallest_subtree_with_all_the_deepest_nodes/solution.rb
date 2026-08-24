# LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

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
def subtree_with_all_deepest(root)
  dfs = lambda do |node|
    return [0, nil] if node.nil?

    ld, ln = dfs.call(node.left)
    rd, rn = dfs.call(node.right)
    return [ld + 1, ln] if ld > rd
    return [rd + 1, rn] if rd > ld

    [ld + 1, node]
  end

  dfs.call(root)[1]
end
