# LeetCode 3995 - Minimum Cost to Convert String III
# https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

# @param {String} source
# @param {String} target
# @param {String[][]} rules
# @param {Integer[]} costs
# @return {Integer}
def min_cost(source, target, rules, costs)
  n = source.length
  return -1 if target.length != n
  inf = 2_147_483_647
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  n.times do |i|
    next if dp[i] == inf
    dp[i + 1] = dp[i] if source[i] == target[i] && dp[i] < dp[i + 1]
    rules.each_with_index do |rule, j|
      p = rule[0]
      r = rule[1]
      plen = p.length
      next if i + plen > n
      c = costs[j]
      ok = true
      plen.times do |k|
        if r[k] != target[i + k]
          ok = false
          break
        end
        if p[k] == "*"
          c += 1
        elsif p[k] != source[i + k]
          ok = false
          break
        end
      end
      dp[i + plen] = dp[i] + c if ok && dp[i] <= inf - c && dp[i] + c < dp[i + plen]
    end
  end
  dp[n] == inf ? -1 : dp[n]
end
