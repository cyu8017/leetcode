# LeetCode 2976 - Minimum Cost to Convert String I
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/

# @param {String} source
# @param {String} target
# @param {Character[]} original
# @param {Character[]} changed
# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(source, target, original, changed, cost)
  inf = 1 << 60
  dist = Array.new(26) { Array.new(26, inf) }
  26.times { |i| dist[i][i] = 0 }
  original.length.times do |i|
    u = original[i][0].ord - 97
    v = changed[i][0].ord - 97
    ww = cost[i]
    dist[u][v] = ww if ww < dist[u][v]
  end
  26.times do |k|
    26.times do |i|
      26.times do |j|
        dist[i][j] = dist[i][k] + dist[k][j] if dist[i][k] + dist[k][j] < dist[i][j]
      end
    end
  end
  ans = 0
  source.length.times do |i|
    a = source[i].ord - 97
    b = target[i].ord - 97
    return -1 if dist[a][b] >= inf / 2

    ans += dist[a][b]
  end
  ans
end
