# LeetCode 2603 - Collect Coins in a Tree
# https://leetcode.com/problems/collect-coins-in-a-tree/

# @param {Integer[]} coins
# @param {Integer[][]} edges
# @return {Integer}
def collect_the_coins(coins, edges)
  n = coins.length
  g = Array.new(n) { {} }
  edges.each do |a, b|
    g[a][b] = true
    g[b][a] = true
  end
  deg = Array.new(n) { |i| g[i].size }
  q = []
  n.times { |i| q << i if deg[i] == 1 && coins[i] == 0 }
  until q.empty?
    u = q.shift
    g[u].keys.each do |v|
      g[v].delete(u)
      deg[v] -= 1
      q << v if deg[v] == 1 && coins[v] == 0
    end
    g[u].clear
    deg[u] = 0
  end
  2.times do
    leaves = (0...n).select { |i| deg[i] == 1 }
    leaves.each do |u|
      g[u].keys.each do |v|
        g[v].delete(u)
        deg[v] -= 1
      end
      g[u].clear
      deg[u] = 0
    end
  end
  remain = 0
  n.times { |i| remain += g[i].size }
  remain
end
