# LeetCode 3299 - Sum of Consecutive Subsequences
# https://leetcode.com/problems/sum-of-consecutive-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def range_sum(nums)
  mod = 1_000_000_007
  cnt = {}
  sm = {}
  ans = 0
  nums.each do |x|
    cl = cnt[x - 1] || 0
    sl = sm[x - 1] || 0
    cr = cnt[x + 1] || 0
    sr = sm[x + 1] || 0
    c = (1 + cl + cr) % mod
    s = (x + sl + (cl * x % mod) + sr + (cr * x % mod)) % mod
    if cl > 0 && cr > 0
      c = (c + (cl * cr % mod)) % mod
      s = (s + (sl * cr % mod) + (sr * cl % mod) + (cl * cr % mod * x % mod)) % mod
    end
    cnt[x] = ((cnt[x] || 0) + c) % mod
    sm[x] = ((sm[x] || 0) + s) % mod
    ans = (ans + s) % mod
  end
  ans
end
