# LeetCode 0685 - Redundant Connection II
# https://leetcode.com/problems/redundant-connection-ii/

# @param {Integer[][]} edges
# @return {Integer[]}
def find_redundant_directed_connection(edges)
  n = edges.length
  parent = Array.new(n + 1, 0)
  cand1 = nil
  cand2 = nil

  edges.each_with_index do |(u, v), i|
    if parent[v] == 0
      parent[v] = u
    else
      cand1 = [parent[v], v]
      cand2 = [u, v]
      edges[i] = [-1, -1]
      break
    end
  end

  uf = (0..n).to_a
  find = lambda do |x|
    while uf[x] != x
      uf[x] = uf[uf[x]]
      x = uf[x]
    end
    x
  end

  edges.each do |u, v|
    next if u < 0

    pu = find.call(u)
    pv = find.call(v)
    return cand1.nil? ? [u, v] : cand1 if pu == pv

    uf[pu] = pv
  end

  cand2.nil? ? [] : cand2
end
