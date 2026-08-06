# LeetCode 1938 - Maximum Genetic Difference Query
# https://leetcode.com/problems/maximum-genetic-difference-query/

# @param {Integer[]} parents
# @param {Integer[][]} queries
# @return {Integer[]}
def max_genetic_difference(parents, queries)
  n = parents.length
  children = Array.new(n) { [] }
  root = 0
  parents.each_with_index do |p, i|
    if p == -1
      root = i
    else
      children[p] << i
    end
  end
  qmap = Array.new(n) { [] }
  queries.each_with_index { |(node, val), i| qmap[node] << [i, val] }
  ans = Array.new(queries.length, 0)
  bits = 17
  trie_root = { child: [nil, nil], cnt: 0 }

  trie_update = lambda do |num, delta|
    node = trie_root
    bits.downto(0) do |b|
      bit = (num >> b) & 1
      node[:child][bit] ||= { child: [nil, nil], cnt: 0 }
      node = node[:child][bit]
      node[:cnt] += delta
    end
  end

  trie_max_xor = lambda do |num|
    node = trie_root
    res = 0
    bits.downto(0) do |b|
      bit = (num >> b) & 1
      want = 1 - bit
      if node[:child][want] && node[:child][want][:cnt] > 0
        res |= 1 << b
        node = node[:child][want]
      else
        node = node[:child][bit]
      end
    end
    res
  end

  dfs = lambda do |u|
    trie_update.call(u, 1)
    qmap[u].each { |qi, val| ans[qi] = trie_max_xor.call(val) }
    children[u].each { |v| dfs.call(v) }
    trie_update.call(u, -1)
  end

  dfs.call(root)
  ans
end
