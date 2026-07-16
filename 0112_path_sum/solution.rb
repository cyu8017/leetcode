class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

def has_path_sum(root, target_sum)
  return false if root.nil?
  return root.val == target_sum if root.left.nil? && root.right.nil?

  has_path_sum(root.left, target_sum - root.val) ||
    has_path_sum(root.right, target_sum - root.val)
end