# LeetCode 1203 - Sort Items by Groups Respecting Dependencies
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

# @param {Integer} n
# @param {Integer} m
# @param {Integer[]} group
# @param {Integer[][]} before_items
# @return {Integer[]}
def sort_items(n, m, group, before_items)
  group = group.dup
  n.times do |i|
    if group[i] == -1
      group[i] = m
      m += 1
    end
  end
  item_graph = Array.new(n) { [] }
  item_indeg = Array.new(n, 0)
  group_graph = Array.new(m) { {} }
  group_indeg = Array.new(m, 0)
  n.times do |v|
    before_items[v].each do |u|
      item_graph[u] << v
      item_indeg[v] += 1
      if group[u] != group[v] && !group_graph[group[u]].key?(group[v])
        group_graph[group[u]][group[v]] = true
        group_indeg[group[v]] += 1
      end
    end
  end
  topo = lambda do |graph, indeg|
    q = indeg.each_index.select { |i| indeg[i] == 0 }
    order = []
    until q.empty?
      u = q.shift
      order << u
      neighbors = graph[u].is_a?(Hash) ? graph[u].keys : graph[u]
      neighbors.each do |v|
        indeg[v] -= 1
        q << v if indeg[v] == 0
      end
    end
    order.length == graph.length ? order : []
  end
  items = topo.call(item_graph, item_indeg)
  groups = topo.call(group_graph, group_indeg)
  return [] if items.empty? || groups.empty?
  buckets = Array.new(m) { [] }
  items.each { |item| buckets[group[item]] << item }
  groups.flat_map { |g| buckets[g] }
end
