# LeetCode 2055 - Plates Between Candles
# https://leetcode.com/problems/plates-between-candles/

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def plates_between_candles(s, queries)
  n = s.length
  pref = Array.new(n + 1, 0)
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  last = -1
  s.each_char.with_index do |ch, i|
    pref[i + 1] = pref[i] + (ch == "*" ? 1 : 0)
    last = i if ch == "|"
    left[i] = last
  end
  last = -1
  (n - 1).downto(0) do |i|
    last = i if s[i] == "|"
    right[i] = last
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(ql, qr), i|
    l = right[ql]
    r = left[qr]
    ans[i] = pref[r] - pref[l] if l != -1 && r != -1 && l < r
  end
  ans
end
