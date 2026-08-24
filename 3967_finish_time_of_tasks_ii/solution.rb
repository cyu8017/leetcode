# LeetCode 3967 - Finish Time of Tasks II
# https://leetcode.com/problems/finish-time-of-tasks-ii/

class Edge
  attr_accessor :to, :reverse

  def initialize(to, reverse)
    @to = to
    @reverse = reverse
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} base_time
# @return {Integer}
def min_finish_time(n, edges, base_time)
  combine = lambda do |minimum, maximum, count, base|
    return base if count == 0
    2 * maximum - minimum + base
  end
  graph = Array.new(n) { [] }
  edges.each do |edge|
    u, v = edge[0], edge[1]
    iu = graph[u].length
    iv = graph[v].length
    graph[u] << Edge.new(v, iv)
    graph[v] << Edge.new(u, iu)
  end
  parent = Array.new(n, -2)
  parent_edge = Array.new(n, 0)
  parent[0] = -1
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    graph[u].each do |edge|
      if parent[edge.to] == -2
        parent[edge.to] = u
        parent_edge[edge.to] = edge.reverse
        order << edge.to
      end
    end
    i += 1
  end
  incoming = Array.new(n) { |i| Array.new(graph[i].length, 0) }
  (n - 1).downto(1) do |oi|
    u = order[oi]
    minimum = 2**62
    maximum = -1
    count = 0
    incoming[u].each_index do |edge_index|
      next if edge_index == parent_edge[u]
      value = incoming[u][edge_index]
      minimum = value if value < minimum
      maximum = value if value > maximum
      count += 1
    end
    value = combine.call(minimum, maximum, count, base_time[u])
    parent_node = parent[u]
    reverse_index = graph[u][parent_edge[u]].reverse
    incoming[parent_node][reverse_index] = value
  end
  answer = 2**62
  order.each do |u|
    min1 = 2**62
    min2 = 2**62
    min_index = -1
    max1 = -1
    max2 = -1
    max_index = -1
    incoming[u].each_with_index do |value, i|
      if value < min1
        min2 = min1
        min1 = value
        min_index = i
      elsif value < min2
        min2 = value
      end
      if value > max1
        max2 = max1
        max1 = value
        max_index = i
      elsif value > max2
        max2 = value
      end
    end
    root_value = combine.call(min1, max1, graph[u].length, base_time[u])
    answer = root_value if root_value < answer
    graph[u].each_with_index do |edge, i|
      next if edge.to == parent[u]
      if graph[u].length == 1
        incoming[edge.to][edge.reverse] = base_time[u]
        next
      end
      minimum = min1
      maximum = max1
      minimum = min2 if i == min_index
      maximum = max2 if i == max_index
      incoming[edge.to][edge.reverse] = combine.call(minimum, maximum, graph[u].length - 1, base_time[u])
    end
  end
  answer
end
