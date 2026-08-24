# LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Boolean}
def is_possible(n, edges)
  deg = Array.new(n + 1, 0)
  adj = Array.new(n + 1) { {} }
  edges.each do |e|
    u = e[0]
    v = e[1]
    deg[u] += 1
    deg[v] += 1
    adj[u][v] = true
    adj[v][u] = true
  end
  odd = (1..n).select { |i| deg[i].odd? }
  return true if odd.empty?

  if odd.length == 2
    a, b = odd
    return true unless adj[a][b]

    (1..n).each do |i|
      return true if i != a && i != b && !adj[a][i] && !adj[b][i]
    end
    return false
  end
  if odd.length == 4
    a, b, c, d = odd
    return (!adj[a][b] && !adj[c][d]) || (!adj[a][c] && !adj[b][d]) || (!adj[a][d] && !adj[b][c])
  end
  false
end
