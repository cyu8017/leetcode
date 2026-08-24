# LeetCode 3802 - Number of Ways to Paint Sheets
# https://leetcode.com/problems/number-of-ways-to-paint-sheets/

# @param {Integer} n
# @param {Integer[]} limit
# @return {Integer}
def number_of_ways(n, limit)
  mod = 1_000_000_007
  limit = limit.sort
  points = [1, n]
  limit.each do |x|
    points << x + 1 if x + 1 > 1 && x + 1 < n
    points << n - x if n - x > 1 && n - x < n
  end
  points.sort!
  u = 0
  (0...points.length).each do |i|
    if u == 0 || points[i] != points[u - 1]
      points[u] = points[i]
      u += 1
    end
  end
  points = points[0, u]
  count_ge = lambda do |lim, x|
    lo = 0
    hi = lim.length
    while lo < hi
      mid = (lo + hi) >> 1
      if lim[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lim.length - lo
  end
  ans = 0
  (0...(points.length - 1)).each do |i|
    x = points[i]
    a = count_ge.call(limit, x)
    b = count_ge.call(limit, n - x)
    same = count_ge.call(limit, [x, n - x].max)
    ways = (a * b - same) % mod
    length = points[i + 1] - x
    ans = (ans + ways * length) % mod
  end
  ans += mod if ans < 0
  ans
end
