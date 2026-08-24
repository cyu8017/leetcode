# LeetCode 3980 - Minimum Operations to Transform Binary String
# https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

# @param {String} s1
# @param {String} s2
# @return {Integer}
def min_operations(s1, s2)
  infinity = 1_000_000_000
  dp = [0, infinity]
  n = s1.length
  n.times do |i|
    nxt = [infinity, infinity]
    2.times do |forced_zero|
      next if dp[forced_zero] == infinity
      current = forced_zero == 1 ? "0" : s1[i]
      direct = dp[forced_zero]
      if current == "0" && s2[i] == "1"
        direct += 1
      elsif current == "1" && s2[i] == "0"
        direct = infinity
      end
      nxt[0] = direct if direct < nxt[0]
      if i + 1 < n
        cost = dp[forced_zero] + 1
        cost += 1 if current == "0"
        cost += 1 if s1[i + 1] == "0"
        cost += 1 if s2[i] == "1"
        nxt[1] = cost if cost < nxt[1]
      end
    end
    dp = nxt
  end
  dp[0] == infinity ? -1 : dp[0]
end
