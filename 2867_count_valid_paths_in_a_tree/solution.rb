# LeetCode 2867 - Count Valid Paths in a Tree
# https://leetcode.com/problems/count-valid-paths-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_paths(n, edges)
  is_prime = Array.new(n + 1, true)
  is_prime[0] = is_prime[1] = false
  i = 2
  while i * i <= n
    if is_prime[i]
      (i * i).step(n, i) { |j| is_prime[j] = false }
    end
    i += 1
  end
  g = Array.new(n + 1) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end

  dfs = lambda do |u, p|
    return 0 if is_prime[u]

    sz = 1
    g[u].each { |v| sz += dfs.call(v, u) if v != p }
    sz
  end

  ans = 0
  (1..n).each do |u|
    next unless is_prime[u]

    total = 0
    g[u].each do |v|
      c = dfs.call(v, u)
      ans += c
      ans += total * c
      total += c
    end
  end
  ans
end
