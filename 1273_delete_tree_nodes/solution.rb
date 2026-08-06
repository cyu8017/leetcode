# LeetCode 1273 - Delete Tree Nodes
# https://leetcode.com/problems/delete-tree-nodes/

# @param {Integer} nodes
# @param {Integer[]} parent
# @param {Integer[]} value
# @return {Integer}
def delete_tree_nodes(nodes, parent, value)
  children = Array.new(nodes) { [] }
  (1...nodes).each { |node| children[parent[node]] << node }
  dfs = nil
  dfs = lambda do |node|
    total = value[node]
    count = 1
    children[node].each do |child|
      child_sum, child_count = dfs.call(child)
      total += child_sum
      count += child_count
    end
    [total, total.zero? ? 0 : count]
  end
  dfs.call(0)[1]
end
