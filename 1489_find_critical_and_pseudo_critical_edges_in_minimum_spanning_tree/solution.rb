# LeetCode 1489 - Find Critical And Pseudo Critical Edges In Minimum Spanning Tree
# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

def find_critical_and_pseudo_critical_edges(n, edges)
  es = edges.each_with_index.map { |(a, b, w), i| [w, a, b, i] }.sort
  mst = lambda do |skip = -1, force = -1|
    parent = (0...n).to_a
    find = lambda do |x|
      while x != parent[x]
        parent[x] = parent[parent[x]]
        x = parent[x]
      end
      x
    end
    total = used = 0
    if force >= 0
      w, a, b, _ = es[force]
      parent[find.call(a)] = find.call(b)
      total += w
      used += 1
    end
    es.each_with_index do |(w, a, b, _), j|
      next if j == skip || j == force
      x = find.call(a)
      y = find.call(b)
      if x != y
        parent[x] = y
        total += w
        used += 1
      end
    end
    used == n - 1 ? total : Float::INFINITY
  end
  base = mst.call
  critical = []
  pseudo = []
  es.each_with_index do |edge, j|
    if mst.call(j) > base
      critical << edge[3]
    elsif mst.call(-1, j) == base
      pseudo << edge[3]
    end
  end
  [critical.sort, pseudo.sort]
end
