# LeetCode 3841 - Palindromic Path Queries in a Tree
# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {String} s
# @param {String[]} queries
# @return {Boolean[]}
def palindromic_path_queries(n, edges, s, queries)
  graph = Array.new(n) { [] }
  edges.each do |edge|
    graph[edge[0]] << edge[1]
    graph[edge[1]] << edge[0]
  end
  parent = Array.new(n, -2)
  depth = Array.new(n, 0)
  parent[0] = -1
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    graph[u].each do |v|
      if parent[v] == -2
        parent[v] = u
        depth[v] = depth[u] + 1
        order << v
      end
    end
    i += 1
  end
  size = Array.new(n, 0)
  heavy = Array.new(n, -1)
  (n - 1).downto(0) do |idx|
    u = order[idx]
    size[u] = 1
    graph[u].each do |v|
      if parent[v] == u
        size[u] += size[v]
        heavy[u] = v if heavy[u] == -1 || size[v] > size[heavy[u]]
      end
    end
  end
  head = Array.new(n, 0)
  position = Array.new(n, 0)
  stack = [[0, 0]]
  next_position = 0
  until stack.empty?
    chain = stack.pop
    u = chain[0]
    while u != -1
      head[u] = chain[1]
      position[u] = next_position
      next_position += 1
      graph[u].each do |v|
        stack << [v, v] if parent[v] == u && v != heavy[u]
      end
      u = heavy[u]
    end
  end
  bit = Array.new(n + 1, 0)

  update = lambda do |index, value|
    index += 1
    while index <= n
      bit[index] ^= value
      index += index & -index
    end
  end

  prefix = lambda do |index|
    result = 0
    while index > 0
      result ^= bit[index]
      index -= index & -index
    end
    result
  end

  path_mask = lambda do |u, v|
    result = 0
    while head[u] != head[v]
      u, v = v, u if depth[head[u]] < depth[head[v]]
      result ^= prefix.call(position[u] + 1) ^ prefix.call(position[head[u]])
      u = parent[head[u]]
    end
    u, v = v, u if position[u] > position[v]
    result ^ prefix.call(position[v] + 1) ^ prefix.call(position[u])
  end

  current = s.chars
  (0...n).each do |node|
    update.call(position[node], 1 << (current[node].ord - 97))
  end
  answer = []
  queries.each do |query|
    parts = query.split(" ")
    op = parts[0]
    node = parts[1].to_i
    if op == "update"
      new_character = parts[2][0]
      delta = (1 << (current[node].ord - 97)) ^ (1 << (new_character.ord - 97))
      update.call(position[node], delta)
      current[node] = new_character
    else
      other = parts[2].to_i
      mask = path_mask.call(node, other)
      answer << ((mask & (mask - 1)) == 0)
    end
  end
  answer
end
