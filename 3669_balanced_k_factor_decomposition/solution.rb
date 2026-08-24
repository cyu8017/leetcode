# LeetCode 3669 - Balanced K-Factor Decomposition
# https://leetcode.com/problems/balanced-k-factor-decomposition/

# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def min_difference(n, k)
  mx = 100_001
  unless defined?($g3669) && $g3669
    g = Array.new(mx) { [] }
    (1...mx).each do |i|
      i.step(mx - 1, i) { |j| g[j] << i }
    end
    $g3669 = g
  end
  g = $g3669
  cur = Float::INFINITY
  ans = []
  path = Array.new(k, 0)
  dfs = nil
  dfs = lambda do |i, x, mi, mxv|
    if i == 0
      d = [mxv, x].max - [mi, x].min
      if d < cur
        cur = d
        path[i] = x
        ans = path.dup
      end
      return
    end
    g[x].each do |y|
      path[i] = y
      dfs.call(i - 1, x / y, [mi, y].min, [mxv, y].max)
    end
  end
  dfs.call(k - 1, n, 10**18, 0)
  ans
end
