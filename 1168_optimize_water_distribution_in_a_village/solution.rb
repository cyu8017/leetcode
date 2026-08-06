# LeetCode 1168 - Optimize Water Distribution in a Village
# https://leetcode.com/problems/optimize-water-distribution-in-a-village/

# @param {Integer} n
# @param {Integer[]} wells
# @param {Integer[][]} pipes
# @return {Integer}
def min_cost_to_supply_water(n, wells, pipes)
  parent = (0..n).to_a
  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  edges = wells.each_with_index.map { |w, i| [0, i + 1, w] } + pipes
  edges.sort_by! { |e| e[2] }
  ans = 0
  edges.each do |a, b, cost|
    ra = find.call(a)
    rb = find.call(b)
    next if ra == rb
    parent[rb] = ra
    ans += cost
  end
  ans
end
