class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

def path_sum(root, target_sum)
  result = []
  visit = lambda do |node, remaining, path|
    next if node.nil?

    current_path = path + [node.val]
    if node.left.nil? && node.right.nil?
      result << current_path if node.val == remaining
    else
      visit.call(node.left, remaining - node.val, current_path)
      visit.call(node.right, remaining - node.val, current_path)
    end
  end
  visit.call(root, target_sum, [])
  result
end