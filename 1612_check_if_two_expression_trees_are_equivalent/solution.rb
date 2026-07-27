# LeetCode 1612 - Check If Two Expression Trees are Equivalent
# https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

class Node
  attr_accessor :val, :left, :right

  def initialize(val = "", left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

def _parse_expr_tree_1612(data)
  return data unless data.is_a?(String)

  inner = data.strip[1...-1]
  vals = inner.nil? || inner.empty? ? [] : inner.split(",")
  nodes = vals.map { |x| x == "null" ? nil : Node.new(x) }
  kids = nodes[1..] || []
  ki = 0
  nodes.each do |node|
    next unless node

    node.left = kids[ki]
    ki += 1
    node.right = kids[ki]
    ki += 1
  end
  nodes[0]
end

def _count_expr_1612(node, out)
  return if node.nil?

  if node.val == "+"
    _count_expr_1612(node.left, out)
    _count_expr_1612(node.right, out)
  else
    out[node.val] += 1
  end
end

# @param {Node|String} root1
# @param {Node|String} root2
# @return {Boolean}
def check_equivalence(root1, root2)
  a = Hash.new(0)
  b = Hash.new(0)
  _count_expr_1612(_parse_expr_tree_1612(root1), a)
  _count_expr_1612(_parse_expr_tree_1612(root2), b)
  a == b
end
