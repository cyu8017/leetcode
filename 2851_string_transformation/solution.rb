# LeetCode 2851 - String Transformation
# https://leetcode.com/problems/string-transformation/

# @param {String} s
# @param {String} t
# @param {Integer} k
# @return {Integer}
def number_of_ways(s, t, k)
  mod = 1_000_000_007
  n = s.length
  ss = s + s
  return 0 unless ss[0, 2 * n - 1].include?(t)

  cnt = 0
  (0...n).each { |i| cnt += 1 if ss[i, n] == t }
  same = s == t

  mod_pow = lambda do |a, b|
    res = 1
    a %= mod
    bb = b
    while bb > 0
      res = (res * a) % mod if (bb & 1) != 0
      a = (a * a) % mod
      bb >>= 1
    end
    res
  end

  pk = mod_pow.call(n - 1, k)
  invn = mod_pow.call(n, mod - 2)
  sign = k.odd? ? (mod - 1) : 1
  ways_same = ((pk + (n - 1) * sign % mod) % mod * invn) % mod
  ways_diff = ((pk - sign + mod) % mod * invn) % mod
  return (ways_same + ways_diff * (cnt - 1)) % mod if same

  (ways_diff * cnt) % mod
end
