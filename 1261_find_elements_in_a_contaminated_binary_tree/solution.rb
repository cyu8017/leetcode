# LeetCode 1261 - Find Elements in a Contaminated Binary Tree
# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

require "set"

class FindElements
  def initialize(root)
    @values = Set.new
    recover = nil
    recover = lambda do |node, value|
      return if node.nil?
      node.val = value
      @values.add(value)
      recover.call(node.left, 2 * value + 1)
      recover.call(node.right, 2 * value + 2)
    end
    recover.call(root, 0)
  end

  def find(target)
    @values.include?(target)
  end
end
