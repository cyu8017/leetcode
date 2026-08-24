# LeetCode 2152 - Minimum Number of Lines to Cover Points
# https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

# @param {Integer[][]} points
# @return {Integer}
def minimum_lines(points)
  n = points.length
  return 1 if n <= 2

  colinear = lambda do |a, b, c|
    (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])
  end
  inf = n
  dp = Array.new(1 << n, inf)
  dp[0] = 0
  (1 << n).times do |mask|
    next if dp[mask] == inf

    i = 0
    i += 1 while i < n && (mask & (1 << i)) != 0
    next if i == n

    nm = mask | (1 << i)
    dp[nm] = [dp[nm], dp[mask] + 1].min
    ((i + 1)...n).each do |j|
      next if (mask & (1 << j)) != 0

      nm = mask | (1 << i) | (1 << j)
      n.times do |k|
        nm |= 1 << k if (nm & (1 << k)).zero? && colinear.call(points[i], points[j], points[k])
      end
      dp[nm] = [dp[nm], dp[mask] + 1].min
    end
  end
  dp[(1 << n) - 1]
end
