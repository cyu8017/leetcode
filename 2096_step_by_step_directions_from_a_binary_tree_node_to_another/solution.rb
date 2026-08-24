# LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} start_value
# @param {Integer} dest_value
# @return {String}
def get_directions(root, start_value, dest_value)
  path = lambda do |node, target, p|
    return false if node.nil?
    return true if node.val == target

    p << "L"
    return true if path.call(node.left, target, p)

    p[-1] = "R"
    return true if path.call(node.right, target, p)

    p.pop
    false
  end

  ps = []
  pd = []
  path.call(root, start_value, ps)
  path.call(root, dest_value, pd)
  i = 0
  i += 1 while i < ps.length && i < pd.length && ps[i] == pd[i]
  ("U" * (ps.length - i)) + pd[i..].join
end
