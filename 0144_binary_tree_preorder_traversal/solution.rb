class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer[]}
def preorder_traversal(root)
  result = []
  traverse = lambda do |node|
    next unless node

    result << node.val
    traverse.call(node.left)
    traverse.call(node.right)
  end
  traverse.call(root)
  result
end