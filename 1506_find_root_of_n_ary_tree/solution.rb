# LeetCode 1506 - Find Root of N-Ary Tree
# https://leetcode.com/problems/find-root-of-n-ary-tree/

# @param {Node[]} tree
# @return {Node}
def find_root(tree)
  value = 0
  nodes = {}
  tree.each do |node|
    nodes[node.val] = node
    value ^= node.val
    node.children.each { |child| value ^= child.val }
  end
  nodes[value]
end
