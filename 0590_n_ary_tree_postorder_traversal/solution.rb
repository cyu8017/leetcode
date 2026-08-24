# LeetCode 0590 - N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

class Node
  attr_accessor :val, :children

  def initialize(val = nil, children = nil)
    @val = val
    @children = children || []
  end
end

def nary_from_list(values)
  return nil if values.nil? || values.empty?

  root = Node.new(values[0], [])
  queue = [root]
  index = values.length > 1 ? 2 : 1
  while !queue.empty? && index < values.length
    node = queue.shift
    while index < values.length && !values[index].nil?
      child = Node.new(values[index], [])
      node.children << child
      queue << child
      index += 1
    end
    index += 1
  end
  root
end

# @param {Node} root
# @return {Integer[]}
def postorder(root)
  root = nary_from_list(root) if root.is_a?(Array)
  result = []

  dfs = lambda do |node|
    return if node.nil?

    (node.children || []).each { |child| dfs.call(child) }
    result << node.val
  end

  dfs.call(root)
  result
end
