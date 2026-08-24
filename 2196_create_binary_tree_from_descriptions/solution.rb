# LeetCode 2196 - Create Binary Tree From Descriptions
# https://leetcode.com/problems/create-binary-tree-from-descriptions/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {Integer[][]} descriptions
# @return {TreeNode}
def create_binary_tree(descriptions)
  nodes = {}
  child = {}
  descriptions.each do |p, c, is_left|
    nodes[p] ||= TreeNode.new(p)
    nodes[c] ||= TreeNode.new(c)
    if is_left == 1
      nodes[p].left = nodes[c]
    else
      nodes[p].right = nodes[c]
    end
    child[c] = true
  end
  nodes.each { |k, v| return v unless child[k] }
  nil
end
