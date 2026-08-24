# LeetCode 3244 - Shortest Distance After Road Addition Queries II
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def shortest_distance_after_queries(n, queries)
  nxt = (1...n).to_a
  cnt = n - 1
  ans = []
  queries.each do |q|
    u = q[0]
    v = q[1]
    if nxt[u] && nxt[u] > 0 && nxt[u] < v
      i = nxt[u]
      while i < v
        cnt -= 1
        ni = nxt[i]
        nxt[i] = 0
        i = ni
      end
      nxt[u] = v
    end
    ans << cnt
  end
  ans
end
