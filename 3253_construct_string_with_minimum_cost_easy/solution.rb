# LeetCode 3253 - Construct String with Minimum Cost (Easy)
# https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

# @param {String} target
# @param {String[]} words
# @param {Integer[]} costs
# @return {Integer}
def minimum_cost(target, words, costs)
  inf = 10**18
  n = target.length
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  best = {}
  words.each_with_index do |w, i|
    best[w] = costs[i] if !best.key?(w) || costs[i] < best[w]
  end
  (0...n).each do |i|
    next if dp[i] == inf
    best.each do |w, c|
      l = w.length
      dp[i + l] = dp[i] + c if i + l <= n && target[i, l] == w && dp[i] + c < dp[i + l]
    end
  end
  dp[n] == inf ? -1 : dp[n]
end
