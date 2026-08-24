# LeetCode 3756 - Concatenate Non Zero Digits and Multiply by Sum II
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def sum_and_multiply(s, queries)
  mx = 100001
  mod = 1_000_000_007
  pw = Array.new(mx, 0)
  pw[0] = 1
  (1...mx).each { |i| pw[i] = pw[i - 1] * 10 % mod }
  n = s.length
  sum_d = Array.new(n + 1, 0)
  cnt_n0 = Array.new(n + 1, 0)
  p = Array.new(n + 1, 0)
  (1..n).each do |i|
    d = s[i - 1].ord - 48
    sum_d[i] = sum_d[i - 1] + d
    cnt_n0[i] = cnt_n0[i - 1]
    if d > 0
      cnt_n0[i] += 1
      p[i] = (p[i - 1] * 10 + d) % mod
    else
      p[i] = p[i - 1]
    end
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(l, r), i|
    n0 = cnt_n0[r + 1] - cnt_n0[l]
    sd = sum_d[r + 1] - sum_d[l]
    x = (p[r + 1] - p[l] * pw[n0] % mod + mod) % mod
    ans[i] = x * sd % mod
  end
  ans
end
