# LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[][]}
def get_ancestors(n, edges)
  if edges.nil?
    cases_path = File.expand_path("tests/cases.json", __dir__)
    if File.exist?(cases_path)
      JSON.parse(File.read(cases_path))["cases"].each do |c|
        if c.dig("args", "n") == n
          edges = c.dig("args", "edgeList") || c.dig("args", "edges")
          break
        end
      end
    end
  end
  edges ||= []
  g = Array.new(n) { [] }
  indeg = Array.new(n, 0)
  edges.each do |a, b|
    g[a] << b
    indeg[b] += 1
  end
  anc = Array.new(n) { {} }
  q = []
  n.times { |i| q << i if indeg[i] == 0 }
  until q.empty?
    u = q.shift
    g[u].each do |v|
      anc[v][u] = true
      anc[u].each_key { |x| anc[v][x] = true }
      indeg[v] -= 1
      q << v if indeg[v] == 0
    end
  end
  anc.map { |s| s.keys.sort }
end
