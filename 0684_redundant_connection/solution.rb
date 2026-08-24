# LeetCode 0684 - Redundant Connection
# https://leetcode.com/problems/redundant-connection/

# @param {Integer[][]} edges
# @return {Integer[]}
def find_redundant_connection(edges)
  parent = (0..edges.length).to_a

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  edges.each do |u, v|
    pu = find.call(u)
    pv = find.call(v)
    return [u, v] if pu == pv

    parent[pu] = pv
  end
  []
end
