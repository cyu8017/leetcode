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
def postorder_traversal(root)
  result = []
  traverse = lambda do |node|
    next unless node

    traverse.call(node.left)
    traverse.call(node.right)
    result << node.val
  end
  traverse.call(root)
  result
end