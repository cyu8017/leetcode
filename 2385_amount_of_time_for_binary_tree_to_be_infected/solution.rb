# LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} start
# @return {Integer}
def amount_of_time(root, start)
  g = {}
  build = lambda do |node, parent|
    return if node.nil?
    if parent
      (g[node.val] ||= []) << parent.val
      (g[parent.val] ||= []) << node.val
    end
    build.call(node.left, node)
    build.call(node.right, node)
  end
  build.call(root, nil)
  ans = 0
  vis = { start => true }
  q = [[start, 0]]
  until q.empty?
    cur, d = q.shift
    ans = d if d > ans
    (g[cur] || []).each do |nxt|
      unless vis[nxt]
        vis[nxt] = true
        q << [nxt, d + 1]
      end
    end
  end
  ans
end
