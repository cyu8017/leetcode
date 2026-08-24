# LeetCode 2764 - Is Array a Preorder of Some Binary Tree
# https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

# @param {Integer[][]} nodes
# @return {Boolean}
def is_preorder(nodes)
  return true if nodes.nil? || nodes.empty?
  stack = [nodes[0][0]]
  (1...nodes.length).each do |i|
    node_id, parent = nodes[i][0], nodes[i][1]
    stack.pop while !stack.empty? && stack[-1] != parent
    return false if stack.empty?
    stack << node_id
  end
  true
end
