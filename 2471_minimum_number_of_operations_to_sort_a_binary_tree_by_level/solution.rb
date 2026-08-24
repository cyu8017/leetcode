# LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

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
def minimum_operations(root)
  return 0 if root.nil?

  ans = 0
  q = [root]
  until q.empty?
    sz = q.length
    vals = Array.new(sz, 0)
    (0...sz).each do |i|
      node = q.shift
      vals[i] = node.val
      q << node.left if node.left
      q << node.right if node.right
    end
    sorted_vals = vals.sort
    pos = {}
    vals.each_with_index { |v, i| pos[v] = i }
    (0...sz).each do |i|
      next if vals[i] == sorted_vals[i]

      j = pos[sorted_vals[i]]
      vals[i], vals[j] = vals[j], vals[i]
      pos[vals[j]] = j
      pos[vals[i]] = i
      ans += 1
    end
  end
  ans
end
