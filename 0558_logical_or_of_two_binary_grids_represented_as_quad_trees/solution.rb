# LeetCode 0558 - Logical OR of Two Binary Grids Represented as Quad-Trees
# https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

class Node
  attr_accessor :val, :isLeaf, :topLeft, :topRight, :bottomLeft, :bottomRight

  def initialize(val = false, is_leaf = false, top_left = nil, top_right = nil, bottom_left = nil, bottom_right = nil)
    @val = val
    @isLeaf = is_leaf
    @topLeft = top_left
    @topRight = top_right
    @bottomLeft = bottom_left
    @bottomRight = bottom_right
  end
end

def list_to_quad(values)
  return nil if values.nil? || values.empty?

  parse = lambda do |data|
    return nil if data.nil?

    Node.new(data[1] == 1 || data[1] == true, data[0] == 1 || data[0] == true)
  end

  root = parse.call(values[0])
  return nil if root.nil?

  queue = [root]
  index = 1
  while !queue.empty? && index < values.length
    node = queue.shift
    next if node.nil?

    children = []
    4.times do
      child = index < values.length ? parse.call(values[index]) : nil
      index += 1
      children << child
      queue << child
    end
    unless node.isLeaf
      node.topLeft, node.topRight, node.bottomLeft, node.bottomRight = children
    end
  end
  root
end

# @param {Node} quad_tree1
# @param {Node} quad_tree2
# @return {Node}
def intersect(quad_tree1, quad_tree2)
  quad_tree1 = list_to_quad(quad_tree1) if quad_tree1.is_a?(Array)
  quad_tree2 = list_to_quad(quad_tree2) if quad_tree2.is_a?(Array)

  return quad_tree1.val ? quad_tree1 : quad_tree2 if quad_tree1.isLeaf
  return quad_tree2.val ? quad_tree2 : quad_tree1 if quad_tree2.isLeaf

  top_left = intersect(quad_tree1.topLeft, quad_tree2.topLeft)
  top_right = intersect(quad_tree1.topRight, quad_tree2.topRight)
  bottom_left = intersect(quad_tree1.bottomLeft, quad_tree2.bottomLeft)
  bottom_right = intersect(quad_tree1.bottomRight, quad_tree2.bottomRight)

  if top_left.isLeaf && top_right.isLeaf && bottom_left.isLeaf && bottom_right.isLeaf &&
     top_left.val == top_right.val && top_left.val == bottom_left.val && top_left.val == bottom_right.val
    return Node.new(top_left.val, true)
  end

  Node.new(false, false, top_left, top_right, bottom_left, bottom_right)
end
