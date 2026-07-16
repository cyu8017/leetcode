class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

def flatten(root)
  return if root.nil?

  flatten(root.left)
  flatten(root.right)
  return if root.left.nil?

  tail = root.left
  tail = tail.right until tail.right.nil?
  tail.right = root.right
  root.right = root.left
  root.left = nil
end