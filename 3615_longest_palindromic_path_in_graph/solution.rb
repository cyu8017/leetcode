# LeetCode 3615 - Longest Palindromic Path in Graph
# https://leetcode.com/problems/longest-palindromic-path-in-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {String} label
# @return {Integer}
def max_len(n, edges, label)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end

  pack = lambda { |a, b| (a << 32) | (b & 0xFFFFFFFF) }

  expand_pal = lambda do |l, r|
    vis = {}
    q = []
    len0 = l != r ? 2 : 1
    q << [l, r, len0]
    best = len0
    vis[pack.call([l, r].min, [l, r].max)] = true
    until q.empty?
      cur0, cur1, cur2 = q.shift
      g[cur0].each do |a|
        g[cur1].each do |b|
          next if a == b || label[a] != label[b]

          p = pack.call([a, b].min, [a, b].max)
          next if vis[p]

          vis[p] = true
          nl = cur2 + 2
          best = nl if nl > best
          q << [a, b, nl]
        end
      end
    end
    best
  end

  ans = 1
  (0...n).each do |i|
    v = expand_pal.call(i, i)
    ans = v if v > ans
    g[i].each do |j|
      if i < j && label[i] == label[j]
        v = expand_pal.call(i, j)
        ans = v if v > ans
      end
    end
  end
  ans
end
