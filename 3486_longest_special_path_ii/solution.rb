# LeetCode 3486 - Longest Special Path II
# https://leetcode.com/problems/longest-special-path-ii/

# @param {Integer[][]} edges
# @param {Integer[]} nums
# @return {Integer[]}
def longest_special_path(edges, nums)
  n = nums.length
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  best_len = 0
  best_nodes = 1
  dfs = nil
  dfs = lambda do |u, p, dist, path_vals, path_dist|
    path_vals << nums[u]
    path_dist << dist
    freq = Hash.new(0)
    dups = 0
    left = 0
    (0...path_vals.length).each do |right|
      v = path_vals[right]
      freq[v] += 1
      dups += 1 if freq[v] == 2
      while dups > 1
        lv = path_vals[left]
        dups -= 1 if freq[lv] == 2
        freq[lv] -= 1
        left += 1
      end
    end
    length = dist - path_dist[left]
    nodes = path_vals.length - left
    if length > best_len || (length == best_len && nodes < best_nodes)
      best_len = length
      best_nodes = nodes
    end
    g[u].each do |v, w|
      next if v == p

      dfs.call(v, u, dist + w, path_vals, path_dist)
    end
    path_vals.pop
    path_dist.pop
  end
  dfs.call(0, -1, 0, [], [])
  [best_len, best_nodes]
end
