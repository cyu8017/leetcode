# LeetCode 1135 - Connecting Cities With Minimum Cost
# https://leetcode.com/problems/connecting-cities-with-minimum-cost/

# @param {Integer} n
# @param {Integer[][]} connections
# @return {Integer}
def minimum_cost(n, connections)
  parent = (0..n).to_a
  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  connections = connections.sort_by { |_, _, w| w }
  cost = 0
  edges = 0
  connections.each do |a, b, w|
    ra = find.call(a)
    rb = find.call(b)
    next if ra == rb
    parent[rb] = ra
    cost += w
    edges += 1
    return cost if edges == n - 1
  end
  -1
end
