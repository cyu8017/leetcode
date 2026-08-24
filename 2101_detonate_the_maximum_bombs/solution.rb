# LeetCode 2101 - Detonate the Maximum Bombs
# https://leetcode.com/problems/detonate-the-maximum-bombs/

# @param {Integer[][]} bombs
# @return {Integer}
def maximum_detonation(bombs)
  n = bombs.length
  g = Array.new(n) { [] }
  n.times do |i|
    x1, y1, r1 = bombs[i]
    n.times do |j|
      next if i == j

      dx = bombs[j][0] - x1
      dy = bombs[j][1] - y1
      g[i] << j if dx * dx + dy * dy <= r1 * r1
    end
  end
  ans = 0
  n.times do |i|
    vis = Array.new(n, false)
    q = [i]
    vis[i] = true
    cnt = 0
    until q.empty?
      u = q.shift
      cnt += 1
      g[u].each do |v|
        unless vis[v]
          vis[v] = true
          q << v
        end
      end
    end
    ans = [ans, cnt].max
  end
  ans
end
