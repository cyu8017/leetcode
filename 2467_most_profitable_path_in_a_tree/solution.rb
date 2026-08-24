# LeetCode 2467 - Most Profitable Path in a Tree
# https://leetcode.com/problems/most-profitable-path-in-a-tree/

# @param {Integer[][]} edges
# @param {Integer} bob
# @param {Integer[]} amount
# @return {Integer}
def most_profitable_path(edges, bob, amount)
  n = amount.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  bob_time = Array.new(n, n)

  find_bob = lambda do |u, p, t|
    if u == 0
      bob_time[u] = t
      return true
    end
    g[u].each do |v|
      next if v == p
      next unless find_bob.call(v, u, t + 1)

      bob_time[u] = t
      return true
    end
    false
  end

  find_bob.call(bob, -1, 0)
  ans = [-(10**18)]

  dfs = lambda do |u, p, t, income|
    cur = amount[u]
    if t > bob_time[u]
      cur = 0
    elsif t == bob_time[u]
      cur /= 2
    end
    income += cur
    is_leaf = true
    g[u].each do |v|
      next if v == p

      is_leaf = false
      dfs.call(v, u, t + 1, income)
    end
    ans[0] = income if is_leaf && income > ans[0]
  end

  dfs.call(0, -1, 0, 0)
  ans[0]
end
