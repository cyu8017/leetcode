class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

def min_depth(root)
  return 0 if root.nil?
  return 1 + min_depth(root.right) if root.left.nil?
  return 1 + min_depth(root.left) if root.right.nil?

  1 + [min_depth(root.left), min_depth(root.right)].min
end