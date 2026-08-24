# LeetCode 0652 - Find Duplicate Subtrees
# https://leetcode.com/problems/find-duplicate-subtrees/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {TreeNode[]}
def find_duplicate_subtrees(root)
  counts = Hash.new(0)
  result = []

  serialize = lambda do |node|
    return "#" if node.nil?

    key = "#{node.val},#{serialize.call(node.left)},#{serialize.call(node.right)}"
    counts[key] += 1
    result << node if counts[key] == 2
    key
  end

  serialize.call(root)
  result.reverse.map { |node| tree_to_list_local(node) }
end

def tree_to_list_local(root)
  return [] if root.nil?

  values = []
  queue = [root]
  until queue.empty?
    node = queue.shift
    if node.nil?
      values << nil
      next
    end
    values << node.val
    queue << node.left
    queue << node.right
  end
  values.pop while !values.empty? && values.last.nil?
  values
end
