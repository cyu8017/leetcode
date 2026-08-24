# LeetCode 3351 - Sum of Good Subsequences
# https://leetcode.com/problems/sum-of-good-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_good_subsequences(nums)
  mod = 1_000_000_007
  cnt = {}
  ssum = {}
  ans = 0
  nums.each do |x|
    c = 1
    s = x
    if (cnt[x - 1] || 0) > 0
      c = (c + cnt[x - 1]) % mod
      s = (s + ssum[x - 1] + cnt[x - 1] * x % mod) % mod
    end
    if (cnt[x + 1] || 0) > 0
      c = (c + cnt[x + 1]) % mod
      s = (s + ssum[x + 1] + cnt[x + 1] * x % mod) % mod
    end
    cnt[x] = ((cnt[x] || 0) + c) % mod
    ssum[x] = ((ssum[x] || 0) + s) % mod
    ans = (ans + s) % mod
  end
  ans
end
