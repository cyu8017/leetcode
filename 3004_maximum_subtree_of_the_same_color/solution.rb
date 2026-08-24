# LeetCode 3004 - Maximum Subtree of the Same Color
# https://leetcode.com/problems/maximum-subtree-of-the-same-color/

# @param {Integer[][]} edges
# @param {Integer[]} colors
# @return {Integer}
def maximum_subtree_size(edges, colors)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  size = Array.new(n, 0)
  ans = 0
  dfs = lambda do |a, fa|
    size[a] = 1
    ok = true
    g[a].each do |b|
      next if b == fa

      t = dfs.call(b, a)
      ok = ok && t && colors[a] == colors[b]
      size[a] += size[b]
    end
    ans = size[a] if ok && size[a] > ans
    ok
  end
  dfs.call(0, -1)
  ans
end

def solve(*args)
  maximum_subtree_size(*args)
end
