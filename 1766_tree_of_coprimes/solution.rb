# LeetCode 1766 - Tree of Coprimes
# https://leetcode.com/problems/tree-of-coprimes/

# @param {Integer[]} nums
# @param {Integer[][]} edges
# @return {Integer[]}
def get_coprimes(nums, edges)
  n = nums.length
  adj = Array.new(n) { [] }
  edges.each do |a, b|
    adj[a] << b
    adj[b] << a
  end
  ans = Array.new(n, -1)
  path = Array.new(51) { [] }
  dfs = lambda do |node, parent, depth|
    best_depth = -1
    best_node = -1
    val = nums[node]
    (1..50).each do |d|
      next unless val.gcd(d) == 1 && !path[d].empty?
      cand_depth, cand_node = path[d].last
      if cand_depth > best_depth
        best_depth = cand_depth
        best_node = cand_node
      end
    end
    ans[node] = best_node
    path[val] << [depth, node]
    adj[node].each do |nxt|
      dfs.call(nxt, node, depth + 1) if nxt != parent
    end
    path[val].pop
  end
  dfs.call(0, -1, 0)
  ans
end
