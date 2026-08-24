# LeetCode 3791 - Number of Balanced Integers in a Range
# https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_balanced(low, high)
  base = 90
  num = ""
  f = []
  dfs = nil
  dfs = lambda do |pos, diff, lim|
    return (diff == 0 ? 1 : 0) if pos >= num.length
    return f[pos][diff + base] if !lim && f[pos][diff + base] != -1
    up = lim ? (num[pos].ord - 48) : 9
    res = 0
    (0..up).each do |i|
      if pos.even?
        res += dfs.call(pos + 1, diff + i, lim && i == up)
      else
        res += dfs.call(pos + 1, diff - i, lim && i == up)
      end
    end
    f[pos][diff + base] = res unless lim
    res
  end
  return 0 if high < 11
  low = 11 if low < 11
  num = (low - 1).to_s
  f = Array.new(20) { Array.new(181, -1) }
  a = dfs.call(0, 0, true)
  num = high.to_s
  f = Array.new(20) { Array.new(181, -1) }
  b = dfs.call(0, 0, true)
  b - a
end
