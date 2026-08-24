# LeetCode 0968 - Binary Tree Cameras
# https://leetcode.com/problems/binary-tree-cameras/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer}
def min_camera_cover(root)
  cameras = [0]
  dfs = lambda do |node|
    return 1 if node.nil?

    left = dfs.call(node.left)
    right = dfs.call(node.right)
    if left == 0 || right == 0
      cameras[0] += 1
      return 2
    end
    return 1 if left == 2 || right == 2

    0
  end
  root_state = dfs.call(root)
  cameras[0] + (root_state == 0 ? 1 : 0)
end
