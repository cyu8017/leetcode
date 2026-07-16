# LeetCode 0095 - Unique Binary Search Trees II
# https://leetcode.com/problems/unique-binary-search-trees-ii/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {Integer} n
# @return {TreeNode[]}
def generate_trees(n)
  return [] if n.zero?

  build(1, n)
end

def build(start_val, end_val)
  return [nil] if start_val > end_val

  trees = []
  (start_val..end_val).each do |root_val|
    left_trees = build(start_val, root_val - 1)
    right_trees = build(root_val + 1, end_val)
    left_trees.each do |left|
      right_trees.each do |right|
        trees << TreeNode.new(root_val, left, right)
      end
    end
  end
  trees
end
