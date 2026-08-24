# LeetCode 3383 - Minimum Runes to Add to Cast Spell
# https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

# @param {Integer} n
# @param {Integer[]} crystals
# @param {Integer[]} flow_from
# @param {Integer[]} flow_to
# @return {Integer}
def min_runes_to_add(n, crystals, flow_from, flow_to)
  g = Array.new(n) { [] }
  rg = Array.new(n) { [] }
  flow_from.length.times do |i|
    a = flow_from[i]
    b = flow_to[i]
    g[a] << b
    rg[b] << a
  end
  vis = Array.new(n, false)
  order = []
  dfs1 = lambda do |u|
    vis[u] = true
    g[u].each { |v| dfs1.call(v) unless vis[v] }
    order << u
  end
  n.times { |i| dfs1.call(i) unless vis[i] }
  comp = Array.new(n, -1)
  cid = 0
  dfs2 = lambda do |u|
    comp[u] = cid
    rg[u].each { |v| dfs2.call(v) if comp[v] == -1 }
  end
  (n - 1).downto(0) do |i|
    u = order[i]
    if comp[u] == -1
      dfs2.call(u)
      cid += 1
    end
  end
  has_crystal = Array.new(cid, false)
  crystals.each { |c| has_crystal[comp[c]] = true }
  indeg = Array.new(cid, 0)
  n.times do |u|
    g[u].each { |v| indeg[comp[v]] += 1 if comp[u] != comp[v] }
  end
  ans = 0
  cid.times { |i| ans += 1 if indeg[i] == 0 && !has_crystal[i] }
  ans
end
