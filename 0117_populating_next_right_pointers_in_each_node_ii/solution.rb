class Node
  attr_accessor :val, :left, :right, :next

  def initialize(val = 0, left = nil, right = nil, next_node = nil)
    @val = val
    @left = left
    @right = right
    @next = next_node
  end
end

def connect(root)
  return root if root.nil?

  level = [root]
  until level.empty?
    level.each_with_index { |node, index| node.next = level[index + 1] }
    level = level.flat_map { |node| [node.left, node.right].compact }
  end
  root
end