# LeetCode 3331 - Find Subtree Sizes After Changes
# https://leetcode.com/problems/find-subtree-sizes-after-changes/

# @param {Integer[]} parent
# @param {String} s
# @return {Integer[]}
def find_subtree_sizes(parent, s)
  n = parent.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[parent[i]] << i }
  new_parent = parent.dup
  last = Array.new(26, -1)
  dfs1 = lambda do |u|
    c = s[u].ord - 97
    prev = last[c]
    new_parent[u] = prev if prev != -1
    last[c] = u
    g[u].each { |v| dfs1.call(v) }
    last[c] = prev
  end
  dfs1.call(0)
  ng = Array.new(n) { [] }
  (1...n).each { |i| ng[new_parent[i]] << i }
  ans = Array.new(n, 0)
  dfs2 = lambda do |u|
    sz = 1
    ng[u].each { |v| sz += dfs2.call(v) }
    ans[u] = sz
    sz
  end
  dfs2.call(0)
  ans
end
