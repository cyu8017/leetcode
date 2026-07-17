# LeetCode 1740 - Find Distance in a Binary Tree
# https://leetcode.com/problems/find-distance-in-a-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} p
# @param {Integer} q
# @return {Integer}
def find_distance(root, p, q)
  graph = Hash.new { |hash, key| hash[key] = [] }
  dfs = lambda do |node, parent|
    return if node.nil?

    graph[node.val]
    if parent
      graph[node.val] << parent.val
      graph[parent.val] << node.val
    end
    dfs.call(node.left, node)
    dfs.call(node.right, node)
  end
  dfs.call(root, nil)
  queue = [[p, 0]]
  seen = { p => true }
  until queue.empty?
    node, dist = queue.shift
    return dist if node == q

    graph[node].each do |nei|
      next if seen[nei]

      seen[nei] = true
      queue << [nei, dist + 1]
    end
  end
  -1
end
