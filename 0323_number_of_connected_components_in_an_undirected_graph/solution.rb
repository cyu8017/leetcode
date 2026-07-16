# LeetCode 0323 - Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class Solution
  def countComponents(n, edges)
    parent = (0...n).to_a
    rank = Array.new(n, 0)

    find = lambda do |node|
      if parent[node] != node
        parent[node] = find.call(parent[node])
      end
      parent[node]
    end

    components = n
    edges.each do |left, right|
      root_left = find.call(left)
      root_right = find.call(right)
      next if root_left == root_right

      if rank[root_left] < rank[root_right]
        root_left, root_right = root_right, root_left
      end
      parent[root_right] = root_left
      rank[root_left] += 1 if rank[root_left] == rank[root_right]
      components -= 1
    end
    components
  end
end
