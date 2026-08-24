# LeetCode 2421 - Number of Good Paths
# https://leetcode.com/problems/number-of-good-paths/

# @param {Integer[]} vals
# @param {Integer[][]} edges
# @return {Integer}
def number_of_good_paths(vals, edges)
  n = vals.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  parent = (0...n).to_a

  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end

  nodes = (0...n).to_a
  nodes.sort_by! { |i| vals[i] }
  ans = n
  i = 0
  while i < n
    j = i
    j += 1 while j < n && vals[nodes[j]] == vals[nodes[i]]
    (i...j).each do |k|
      u = nodes[k]
      g[u].each do |v|
        next if vals[v] > vals[u]

        ru = find.call(u)
        rv = find.call(v)
        parent[ru] = rv if ru != rv
      end
    end
    freq = Hash.new(0)
    (i...j).each { |k| freq[find.call(nodes[k])] += 1 }
    freq.each_value { |c| ans += c * (c - 1) / 2 }
    i = j
  end
  ans
end
