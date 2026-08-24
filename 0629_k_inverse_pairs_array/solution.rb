# LeetCode 0629 - K Inverse Pairs Array
# https://leetcode.com/problems/k-inverse-pairs-array/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def k_inverse_pairs(n, k)
  mod = 10**9 + 7
  dp = Array.new(k + 1, 0)
  dp[0] = 1

  (1..n).each do |size|
    nxt = Array.new(k + 1, 0)
    prefix = 0
    (0..k).each do |pairs|
      prefix = (prefix + dp[pairs]) % mod
      prefix = (prefix - dp[pairs - size]) % mod if pairs >= size
      nxt[pairs] = prefix
    end
    dp = nxt
  end

  dp[k]
end
