# LeetCode 0559 - Maximum Depth of N-ary Tree
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Node
  attr_accessor :val, :children

  def initialize(val = nil, children = nil)
    @val = val
    @children = children || []
  end
end

# @param {Node} root
# @return {Integer}
def max_depth(root)
  return 0 if root.nil?
  return 1 if root.children.nil? || root.children.empty?

  1 + root.children.map { |child| max_depth(child) }.max
end
