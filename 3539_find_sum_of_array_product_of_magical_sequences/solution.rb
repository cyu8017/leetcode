# LeetCode 3539 - Find Sum of Array Product of Magical Sequences
# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

# @param {Integer} m
# @param {Integer} k
# @param {Integer[]} nums
# @return {Integer}
def magical_sum(m, k, nums)
  nn = 31
  mod = 1000000007
  f = Array.new(nn, 0)
  g = Array.new(nn, 0)
  qpow = lambda do |a, kk|
    res = 1
    ba = a
    bk = kk
    while bk > 0
      res = res * ba % mod if (bk & 1) != 0
      ba = ba * ba % mod
      bk >>= 1
    end
    res
  end
  f[0] = g[0] = 1
  (1...nn).each do |i|
    f[i] = f[i - 1] * i % mod
    g[i] = qpow.call(f[i], mod - 2)
  end
  comb = lambda do |mm, nnn|
    return 0 if nnn < 0 || nnn > mm
    f[mm] * g[nnn] % mod * g[mm - nnn] % mod
  end
  n = nums.length
  dp = Array.new(n + 1) { Array.new(m + 1) { Array.new(k + 1) { Array.new(nn, -1) } } }
  dfs = nil
  dfs = lambda do |i, j, kk, st|
    return 0 if kk < 0 || (i == n && j > 0)
    if i == n
      while st > 0
        kk -= st & 1
        st >>= 1
      end
      return kk == 0 ? 1 : 0
    end
    return dp[i][j][kk][st] if dp[i][j][kk][st] != -1
    res = 0
    (0..j).each do |t|
      nt = t + st
      nk = kk - (nt & 1)
      p = qpow.call(nums[i], t)
      tmp = comb.call(j, t) * p % mod * dfs.call(i + 1, j - t, nk, nt >> 1) % mod
      res = (res + tmp) % mod
    end
    dp[i][j][kk][st] = res
    res
  end
  dfs.call(0, m, k, 0)
end
