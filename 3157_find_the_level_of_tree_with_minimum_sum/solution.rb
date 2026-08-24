# LeetCode 3157 - Find the Level of Tree with Minimum Sum
# https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

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
def minimum_level(root)
  q = [root]
  s = 10**18
  ans = 0
  level = 1
  until q.empty?
    t = 0
    m = q.length
    while m > 0
      node = q.shift
      t += node.val
      q << node.left if node.left
      q << node.right if node.right
      m -= 1
    end
    if s > t
      s = t
      ans = level
    end
    level += 1
  end
  ans
end
