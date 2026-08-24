# LeetCode 3588 - Find Maximum Area of a Triangle
# https://leetcode.com/problems/find-maximum-area-of-a-triangle/

# @param {Integer[][]} coords
# @return {Integer}
def max_area(coords)
  calc = lambda do |cs|
    mn = 10**9
    mx = 0
    f = {}
    g = {}
    cs.each do |c|
      x, y = c[0], c[1]
      mn = [mn, x].min
      mx = [mx, x].max
      if f.key?(x)
        f[x] = [f[x], y].min
        g[x] = [g[x], y].max
      else
        f[x] = y
        g[x] = y
      end
    end
    ans = 0
    f.each do |x, y|
      d = g[x] - y
      ans = [ans, d * [mx - x, x - mn].max].max
    end
    ans
  end
  ans = calc.call(coords)
  coords.each { |c| c[0], c[1] = c[1], c[0] }
  ans = [ans, calc.call(coords)].max
  ans > 0 ? ans : -1
end
