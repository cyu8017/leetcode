# LeetCode 3425 - Longest Special Path
# https://leetcode.com/problems/longest-special-path/

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
  last = {}
  path = []
  dfs = nil
  dfs = lambda do |u, p, dist, left|
    seen = last.key?(nums[u])
    prev_pos = seen ? last[nums[u]] : -1
    last[nums[u]] = path.length
    new_left = left
    new_left = prev_pos + 1 if seen && prev_pos >= left
    path << dist
    length = dist - path[new_left]
    nodes = path.length - new_left
    if length > best_len || (length == best_len && nodes < best_nodes)
      best_len = length
      best_nodes = nodes
    end
    g[u].each do |v, w|
      next if v == p

      dfs.call(v, u, dist + w, new_left)
    end
    path.pop
    if seen
      last[nums[u]] = prev_pos
    else
      last.delete(nums[u])
    end
  end
  dfs.call(0, -1, 0, 0)
  [best_len, best_nodes]
end
