# LeetCode 2581 - Count Number of Possible Root Nodes
# https://leetcode.com/problems/count-number-of-possible-root-nodes/

# @param {Integer[][]} edges
# @param {Integer[][]} guesses
# @param {Integer} k
# @return {Integer}
def root_count(edges, guesses, k)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  guess_set = {}
  guesses.each { |a, b| guess_set["#{a},#{b}"] = true }

  dfs1 = nil
  dfs1 = lambda do |u, p|
    cnt = 0
    g[u].each do |v|
      next if v == p

      cnt += 1 if guess_set["#{u},#{v}"]
      cnt += dfs1.call(v, u)
    end
    cnt
  end

  ans = 0
  dfs2 = nil
  dfs2 = lambda do |u, p, cur|
    ans += 1 if cur >= k
    g[u].each do |v|
      next if v == p

      nxt = cur
      nxt -= 1 if guess_set["#{u},#{v}"]
      nxt += 1 if guess_set["#{v},#{u}"]
      dfs2.call(v, u, nxt)
    end
  end

  dfs2.call(0, -1, dfs1.call(0, -1))
  ans
end
