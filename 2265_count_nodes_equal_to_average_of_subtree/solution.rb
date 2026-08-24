# LeetCode 2265 - Count Nodes Equal to Average of Subtree
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer}
def average_of_subtree(root)
  ans = 0
  dfs = lambda do |node|
    return [0, 0] if node.nil?

    ls, lc = dfs.call(node.left)
    rs, rc = dfs.call(node.right)
    total = ls + rs + node.val
    cnt = lc + rc + 1
    ans += 1 if total / cnt == node.val
    [total, cnt]
  end
  dfs.call(root)
  ans
end
