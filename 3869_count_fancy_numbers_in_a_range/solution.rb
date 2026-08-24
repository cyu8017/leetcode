# LeetCode 3869 - Count Fancy Numbers in a Range
# https://leetcode.com/problems/count-fancy-numbers-in-a-range/

# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def count_fancy(l, r)
  check = lambda do |s|
    return s % 11 != 0 if s < 100
    mid = (s / 10) % 10
    last = s % 10
    mid > 1 && mid < last
  end
  num = ""
  n = 0
  f = []
  dfs = nil
  dfs = lambda do |pos, s, prev, st, lim|
    if pos >= n
      return st != 3 ? 1 : (check.call(s) ? 1 : 0)
    end
    return f[pos][s][prev][st] if !lim && f[pos][s][prev][st] != -1
    up = lim ? num[pos].ord - 48 : 9
    res = 0
    (0..up).each do |i|
      nxt_st = st
      if st == 0
        nxt_st = if prev == 0
                   0
                 elsif i > prev
                   1
                 elsif i < prev
                   2
                 else
                   3
                 end
      elsif st == 1
        nxt_st = i > prev ? 1 : 3
      elsif st == 2
        nxt_st = i < prev ? 2 : 3
      else
        nxt_st = 3
      end
      res += dfs.call(pos + 1, s + i, i, nxt_st, lim && i == up)
    end
    f[pos][s][prev][st] = res unless lim
    res
  end
  calc = lambda do |x|
    return 0 if x < 0
    num = x.to_s
    n = num.length
    f = Array.new(n) { Array.new(9 * n + 1) { Array.new(10) { Array.new(4, -1) } } }
    dfs.call(0, 0, 0, 0, true)
  end
  calc.call(r) - calc.call(l - 1)
end
