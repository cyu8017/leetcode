# LeetCode 0863 - All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {TreeNode} target
# @param {Integer} k
# @return {Integer[]}
def distance_k(root, target, k)
  graph = Hash.new { |h, k| h[k] = [] }

  build = lambda do |node, parent|
    return if node.nil?

    build.call(node.left, node)
    build.call(node.right, node)
    if parent
      graph[node] << parent
      graph[parent] << node
    end
  end

  build.call(root, nil)

  unless target.respond_to?(:val)
    find = lambda do |node|
      return nil if node.nil?
      return node if node.val == target

      find.call(node.left) || find.call(node.right)
    end
    target = find.call(root)
  end

  queue = [[target, 0]]
  seen = { target => true }
  ans = []
  until queue.empty?
    node, dist = queue.shift
    if dist == k
      ans << node.val
      next
    end
    graph[node].each do |nei|
      next if seen[nei]

      seen[nei] = true
      queue << [nei, dist + 1]
    end
  end
  ans
end
