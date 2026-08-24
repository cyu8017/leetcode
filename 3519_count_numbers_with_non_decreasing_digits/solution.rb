# LeetCode 3519 - Count Numbers with Non-Decreasing Digits
# https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

# @param {String} l
# @param {String} r
# @param {Integer} b
# @return {Integer}
def count_numbers(l, r, b)
  mod = 1000000007
  to_digits = lambda do |s, base|
    return [0] if s == "0"
    digs = []
    until s.length == 1 && s[0] == "0"
      rem = 0
      q = ""
      s.each_char do |c|
        cur = rem * 10 + (c.ord - 48)
        d = cur / base
        rem = cur % base
        q += d.to_s if q.length > 0 || d != 0
      end
      digs << rem
      s = q.empty? ? "0" : q
    end
    digs.reverse
  end
  dec = lambda do |s|
    a = s.chars
    i = a.length - 1
    while i >= 0 && a[i] == "0"
      a[i] = "9"
      i -= 1
    end
    return "0" if i < 0
    a[i] = (a[i].ord - 49).chr
    t = a.join
    p = 0
    p += 1 while p + 1 < t.length && t[p] == "0"
    t[p..]
  end
  count_upto = lambda do |digs, base|
    m = digs.length
    memo = {}
    dfs = nil
    dfs = lambda do |pos, last, tight|
      return 1 if pos == m
      key = [pos, last, tight ? 1 : 0]
      return memo[key] if memo.key?(key)
      up = tight ? digs[pos] : base - 1
      res = 0
      (last..up).each do |d|
        res = (res + dfs.call(pos + 1, d, tight && d == up)) % mod
      end
      memo[key] = res
      res
    end
    dfs.call(0, 0, true)
  end
  rd = to_digits.call(r, b)
  ld = to_digits.call(dec.call(l), b)
  (count_upto.call(rd, b) - count_upto.call(ld, b) + mod) % mod
end
