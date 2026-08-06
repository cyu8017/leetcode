# LeetCode 1361 - Validate Binary Tree Nodes
# https://leetcode.com/problems/validate-binary-tree-nodes/

def validate_binary_tree_nodes(n, left_child, right_child)
  indeg = Array.new(n, 0)
  (left_child + right_child).each do |x|
    next if x == -1
    indeg[x] += 1
    return false if indeg[x] > 1
  end
  roots = indeg.each_index.select { |i| indeg[i] == 0 }
  return false if roots.length != 1
  seen = {}
  st = roots.dup
  until st.empty?
    u = st.pop
    return false if seen[u]
    seen[u] = true
    [left_child[u], right_child[u]].each { |v| st << v if v != -1 }
  end
  seen.length == n
end
