# LeetCode 3352 - Count K-Reducible Numbers Less Than N
# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

# @param {Integer} x
# @return {Integer}
def bits_pop(x)
  c = 0
  while x > 0
    c += x & 1
    x >>= 1
  end
  c
end

# @param {String} s
# @param {Integer} k
# @return {Integer}
def count_k_reducible_numbers(s, k)
  mod = 1_000_000_007
  red = Array.new(801, 0)
  red[1] = 0
  (2...801).each { |i| red[i] = 1 + red[bits_pop(i)] }
  memo = {}
  dfs = lambda do |pos, tight, ones|
    if pos == s.length
      return 0 if ones == 0
      return red[ones] <= k - 1 ? 1 : 0
    end
    ky = (pos << 32) | ((tight ? 1 : 0) << 16) | ones
    return memo[ky] if memo.key?(ky)

    up = tight ? (s[pos].ord - 48) : 1
    ans = 0
    (0..up).each do |d|
      nt = tight && d == up
      ans = (ans + dfs.call(pos + 1, nt, ones + d)) % mod
    end
    memo[ky] = ans
    ans
  end
  dfs.call(0, true, 0)
end
