# LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def minimum_changes(s, k)
  n = s.length
  inf = 1 << 20
  cost = Array.new(n) { Array.new(n, inf) }

  semi_cost = lambda do |l, r|
    length = r - l + 1
    best = inf
    (1...length).each do |d|
      next unless length % d == 0

      chg = 0
      (0...d).each do |start|
        chars = []
        i = l + start
        while i <= r
          chars << s[i]
          i += d
        end
        i = 0
        j = chars.length - 1
        while i < j
          chg += 1 if chars[i] != chars[j]
          i += 1
          j -= 1
        end
      end
      best = chg if chg < best
    end
    best
  end

  (0...n).each do |i|
    (i + 1...n).each { |j| cost[i][j] = semi_cost.call(i, j) }
  end
  dp = Array.new(k + 1) { Array.new(n + 1, inf) }
  dp[0][0] = 0
  (1..k).each do |p|
    (1..n).each do |i|
      (0...i - 1).each do |t|
        cand = dp[p - 1][t] + cost[t][i - 1]
        dp[p][i] = cand if cand < dp[p][i]
      end
    end
  end
  dp[k][n]
end
