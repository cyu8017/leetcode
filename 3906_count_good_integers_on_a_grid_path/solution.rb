# LeetCode 3906 - Count Good Integers on a Grid Path
# https://leetcode.com/problems/count-good-integers-on-a-grid-path/

# @param {Integer} l
# @param {Integer} r
# @param {String} directions
# @return {Integer}
def count_good_integers_on_path(l, r, directions)
  key = Array.new(16, false)
  row = 0
  col = 0
  key[0] = true
  directions.each_char do |c|
    if c == "D"
      row += 1
    else
      col += 1
    end
    key[row * 4 + col] = true
  end
  s = ""
  f = []
  dfs = nil
  dfs = lambda do |pos, last, lim|
    return 1 if pos == 16
    return f[pos][last] if !lim && f[pos][last] != -1
    res = 0
    start = key[pos] ? last : 0
    endv = lim ? s[pos].ord - 48 : 9
    (start..endv).each do |i|
      next_last = key[pos] ? i : last
      res += dfs.call(pos + 1, next_last, lim && i == endv)
    end
    f[pos][last] = res unless lim
    res
  end
  calc = lambda do |x|
    return 0 if x < 0
    t = x.to_s
    s = "0" * (16 - t.length) + t
    f = Array.new(16) { Array.new(10, -1) }
    dfs.call(0, 0, true)
  end
  calc.call(r) - calc.call(l - 1)
end
