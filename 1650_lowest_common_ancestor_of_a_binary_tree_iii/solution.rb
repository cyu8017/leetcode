# LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

# @param {Object} p
# @param {Object} q
# @return {Object}
def lowest_common_ancestor(p, q)
  compatibility = p.is_a?(Hash) && p.key?("tree")
  if compatibility
    data = p
    vals = data["tree"]
    nodes = vals.map { |v| v.nil? ? nil : Struct.new(:val, :left, :right, :parent).new(v, nil, nil, nil) }
    nodes.each_with_index do |node, i|
      next if node.nil?
      left_i = 2 * i + 1
      right_i = 2 * i + 2
      if left_i < nodes.length && nodes[left_i]
        node.left = nodes[left_i]
        nodes[left_i].parent = node
      end
      if right_i < nodes.length && nodes[right_i]
        node.right = nodes[right_i]
        nodes[right_i].parent = node
      end
    end
    p = nodes.find { |x| x && x.val == data["p"] }
    q = nodes.find { |x| x && x.val == data["q"] }
  end
  a = p
  b = q
  while a != b
    a = a ? a.parent : q
    b = b ? b.parent : p
  end
  compatibility ? a.val : a
end
