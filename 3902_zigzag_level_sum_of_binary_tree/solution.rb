# LeetCode 3902 - Zigzag Level Sum of Binary Tree
# https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer[]}
def zigzag_level_sum(root)
  ans = []
  q = [root]
  left = true
  until q.empty?
    nq = []
    q.each do |node|
      nq << node.left if node.left
      nq << node.right if node.right
    end
    m = q.length
    s = 0
    m.times do |i|
      node = left ? q[i] : q[m - i - 1]
      child = left ? node.left : node.right
      break unless child
      s += node.val
    end
    ans << s
    left = !left
    q = nq
  end
  ans
end
