# LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
# https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

# @param {Integer[]} nums
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def count_sub_multisets(nums, l, r)
  mod = 1_000_000_007
  freq = {}
  total = 0
  nums.each do |v|
    freq[v] = freq.fetch(v, 0) + 1
    total += v
  end
  return 0 if total < l

  r = total if r > total
  dp = Array.new(r + 1, 0)
  dp[0] = 1
  zeros = freq.fetch(0, 0)
  freq.delete(0)
  freq.each do |v, c|
    ndp = Array.new(r + 1, 0)
    (0..r).each do |s|
      next if dp[s] == 0

      k = 0
      while k <= c && s + k * v <= r
        ndp[s + k * v] = (ndp[s + k * v] + dp[s]) % mod
        k += 1
      end
    end
    dp = ndp
  end
  ans = 0
  (l..r).each { |s| ans = (ans + dp[s]) % mod }
  (ans * (zeros + 1)) % mod
end
