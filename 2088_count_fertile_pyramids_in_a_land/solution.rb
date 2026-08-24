# LeetCode 2088 - Count Fertile Pyramids in a Land
# https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

# @param {Integer[][]} grid
# @return {Integer}
def count_pyramids(grid)
  count = lambda do |g|
    m = g.length
    n = g[0].length
    dp = g.map(&:dup)
    ans = 0
    (m - 2).downto(0) do |i|
      (1...n - 1).each do |j|
        next unless g[i][j] == 1

        dp[i][j] = 1 + [dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1]].min
        ans += dp[i][j] - 1
      end
    end
    ans
  end
  count.call(grid) + count.call(grid.reverse)
end
