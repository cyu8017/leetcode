# LeetCode 3249 - Count the Number of Good Nodes
# https://leetcode.com/problems/count-the-number-of-good-nodes/

# @param {Integer[][]} edges
# @return {Integer}
def count_good_nodes(edges)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  ans = 0
  dfs = nil
  dfs = lambda do |a, fa|
    pre = -1
    cnt = 1
    ok = 1
    g[a].each do |b|
      next if b == fa
      cur = dfs.call(b, a)
      cnt += cur
      if pre < 0
        pre = cur
      elsif pre != cur
        ok = 0
      end
    end
    ans += ok
    cnt
  end
  dfs.call(0, -1)
  ans
end
