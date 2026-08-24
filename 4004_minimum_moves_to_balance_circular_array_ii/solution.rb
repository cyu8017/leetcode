# LeetCode 4004 - Minimum Moves to Balance Circular Array II
# https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

class Edge
  attr_accessor :to, :cap, :cost, :rev

  def initialize(to, cap, cost, rev)
    @to = to
    @cap = cap
    @cost = cost
    @rev = rev
  end
end

class MinCostMaxFlow
  def initialize(n_)
    @n = n_
    @graph = Array.new(n_) { [] }
  end

  def add_edge(u, v, cap, cost)
    @graph[u] << Edge.new(v, cap, cost, @graph[v].length)
    @graph[v] << Edge.new(u, 0, -cost, @graph[u].length - 1)
  end

  def min_cost_flow(source, sink, max_flow)
    inf = 1_000_000_000
    total_cost = 0
    current_flow = 0
    n = @n
    graph = @graph
    while current_flow < max_flow
      dist = Array.new(n, inf)
      parent_node = Array.new(n, -1)
      parent_edge = Array.new(n, -1)
      in_queue = Array.new(n, false)
      q = [source]
      dist[source] = 0
      in_queue[source] = true
      qi = 0
      while qi < q.length
        u = q[qi]
        qi += 1
        in_queue[u] = false
        graph[u].each_with_index do |e, i|
          if e.cap > 0 && dist[e.to] > dist[u] + e.cost
            dist[e.to] = dist[u] + e.cost
            parent_node[e.to] = u
            parent_edge[e.to] = i
            unless in_queue[e.to]
              in_queue[e.to] = true
              q << e.to
            end
          end
        end
      end
      return -1 if dist[sink] == inf
      push_flow = max_flow - current_flow
      cur = sink
      while cur != source
        e = graph[parent_node[cur]][parent_edge[cur]]
        push_flow = e.cap if e.cap < push_flow
        cur = parent_node[cur]
      end
      cur = sink
      while cur != source
        p = parent_node[cur]
        idx = parent_edge[cur]
        rev = graph[p][idx].rev
        graph[p][idx].cap -= push_flow
        graph[cur][rev].cap += push_flow
        cur = parent_node[cur]
      end
      current_flow += push_flow
      total_cost += push_flow * dist[sink]
    end
    total_cost
  end
end

# @param {Integer[]} balance
# @return {Integer}
def min_moves(balance)
  inf = 1_000_000_000
  total_balance = 0
  total_deficit = 0
  balance.each do |x|
    total_balance += x
    total_deficit += -x if x < 0
  end
  return -1 if total_balance < 0
  return 0 if total_deficit == 0
  n = balance.length
  source = n
  sink = n + 1
  mcmf = MinCostMaxFlow.new(n + 2)
  n.times do |i|
    x = balance[i]
    if x > 0
      mcmf.add_edge(source, i, x, 0)
    elsif x < 0
      mcmf.add_edge(i, sink, -x, 0)
    end
    mcmf.add_edge(i, (i + 1) % n, inf, 1)
    mcmf.add_edge(i, (i - 1 + n) % n, inf, 1)
  end
  mcmf.min_cost_flow(source, sink, total_deficit)
end
