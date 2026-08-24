# LeetCode 2492 - Minimum Score of a Path Between Two Cities
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def min_score(n, roads)
  g = Array.new(n + 1) { [] }
  roads.each do |r|
    g[r[0]] << [r[1], r[2]]
    g[r[1]] << [r[0], r[2]]
  end
  vis = Array.new(n + 1, false)
  ans = 1 << 30
  q = [1]
  vis[1] = true
  until q.empty?
    u = q.shift
    g[u].each do |v, w|
      ans = w if w < ans
      unless vis[v]
        vis[v] = true
        q << v
      end
    end
  end
  ans
end
