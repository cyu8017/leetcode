# LeetCode 3179 - Find the N-th Value After K Seconds
# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def value_after_k_seconds(n, k)
  mod = 1_000_000_007
  a = Array.new(n, 1)
  while k > 0
    (1...n).each { |i| a[i] = (a[i] + a[i - 1]) % mod }
    k -= 1
  end
  a[n - 1]
end
