# LeetCode 0742 - Closest Leaf in a Binary Tree
# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def find_closest_leaf(root, k)
  graph = Hash.new { |h, key| h[key] = [] }
  leaves = {}

  build = lambda do |node, parent|
    return if node.nil?

    if parent
      graph[node.val] << parent.val
      graph[parent.val] << node.val
    end
    leaves[node.val] = true if node.left.nil? && node.right.nil?
    build.call(node.right, node)
    build.call(node.left, node)
  end

  build.call(root, nil)
  queue = [k]
  seen = { k => true }
  until queue.empty?
    value = queue.shift
    return value if leaves[value]

    graph[value].each do |neighbor|
      next if seen[neighbor]

      seen[neighbor] = true
      queue << neighbor
    end
  end
  -1
end
