# LeetCode 1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

def num_of_arrays(n, m, k)
  mod = 1_000_000_007
  dp = Array.new(k + 1) { Array.new(m + 1, 0) }
  (1..m).each { |maximum| dp[1][maximum] = 1 }
  (1...n).each do
    nxt = Array.new(k + 1) { Array.new(m + 1, 0) }
    (1..k).each do |cost|
      prefix = 0
      (1..m).each do |maximum|
        prefix = (prefix + dp[cost - 1][maximum - 1]) % mod
        nxt[cost][maximum] = (maximum * dp[cost][maximum] + prefix) % mod
      end
    end
    dp = nxt
  end
  dp[k].sum % mod
end
