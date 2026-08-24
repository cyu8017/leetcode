# LeetCode 2977 - Minimum Cost to Convert String II
# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

# @param {String} source
# @param {String} target
# @param {String[]} original
# @param {String[]} changed
# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(source, target, original, changed, cost)
  inf = 1 << 60
  ids = {}
  original.length.times do |i|
    ids[original[i]] = ids.length unless ids.key?(original[i])
    ids[changed[i]] = ids.length unless ids.key?(changed[i])
  end
  m = ids.length
  dist = Array.new(m) { Array.new(m, inf) }
  m.times { |i| dist[i][i] = 0 }
  original.length.times do |i|
    u = ids[original[i]]
    v = ids[changed[i]]
    ww = cost[i]
    dist[u][v] = ww if ww < dist[u][v]
  end
  m.times do |k|
    m.times do |i|
      m.times do |j|
        dist[i][j] = dist[i][k] + dist[k][j] if dist[i][k] + dist[k][j] < dist[i][j]
      end
    end
  end
  n = source.length
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  lens = {}
  ids.each_key { |key| lens[key.length] = true }
  n.times do |i|
    next if dp[i] >= inf / 2

    dp[i + 1] = dp[i] if source[i] == target[i] && dp[i] < dp[i + 1]
    lens.each_key do |len|
      next if i + len > n

      ss = source[i, len]
      tt = target[i, len]
      next unless ids.key?(ss) && ids.key?(tt)

      iu = ids[ss]
      iv = ids[tt]
      if dist[iu][iv] < inf / 2
        cand = dp[i] + dist[iu][iv]
        dp[i + len] = cand if cand < dp[i + len]
      end
    end
  end
  return -1 if dp[n] >= inf / 2

  dp[n]
end
