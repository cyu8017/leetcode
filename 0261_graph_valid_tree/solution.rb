# LeetCode 0261 - Graph Valid Tree
# https://leetcode.com/problems/graph-valid-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Boolean}
def valid_tree(n, edges)
  return false if edges.length != n - 1

  parent = (0...n).to_a

  find = lambda do |node|
    if parent[node] != node
      parent[node] = find.call(parent[node])
    end
    parent[node]
  end

  edges.each do |left, right|
    root_left = find.call(left)
    root_right = find.call(right)
    return false if root_left == root_right

    parent[root_left] = root_right
  end
  true
end
