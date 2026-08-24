# LeetCode 3548 - Equal Sum Grid Partition II
# https://leetcode.com/problems/equal-sum-grid-partition-ii/

# @param {Integer[][]} grid
# @return {Boolean}
def can_partition_grid(grid)
  rotate = lambda do |g|
    m = g.length
    n = g[0].length
    t = Array.new(n) { Array.new(m, 0) }
    (0...m).each { |i| (0...n).each { |j| t[j][i] = g[i][j] } }
    t
  end
  check = lambda do |g|
    m = g.length
    n = g[0].length
    s1 = 0
    s2 = 0
    cnt1 = {}
    cnt2 = {}
    g.each do |row|
      row.each do |x|
        s2 += x
        cnt2[x] = (cnt2[x] || 0) + 1
      end
    end
    (0...(m - 1)).each do |i|
      g[i].each do |x|
        s1 += x
        s2 -= x
        cnt1[x] = (cnt1[x] || 0) + 1
        cnt2[x] = (cnt2[x] || 0) - 1
      end
      return true if s1 == s2
      if s1 < s2
        diff = s2 - s1
        if (cnt2[diff] || 0) > 0
          if (m - i - 1 > 1 && n > 1) ||
             (i == m - 2 && (g[i + 1][0] == diff || g[i + 1][n - 1] == diff)) ||
             (n == 1 && (g[i + 1][0] == diff || g[m - 1][0] == diff))
            return true
          end
        end
      else
        diff = s1 - s2
        if (cnt1[diff] || 0) > 0
          if (i + 1 > 1 && n > 1) ||
             (i == 0 && (g[0][0] == diff || g[0][n - 1] == diff)) ||
             (n == 1 && (g[0][0] == diff || g[i][0] == diff))
            return true
          end
        end
      end
    end
    false
  end
  check.call(grid) || check.call(rotate.call(grid))
end
