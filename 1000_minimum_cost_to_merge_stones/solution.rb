# LeetCode 1000 - Minimum Cost to Merge Stones
# https://leetcode.com/problems/minimum-cost-to-merge-stones/

# @param {Integer[]} stones
# @param {Integer} k
# @return {Integer}
def merge_stones(stones, k)
  n = stones.length
  return -1 if (n - 1) % (k - 1) != 0

  prefix = [0]
  stones.each { |x| prefix << prefix[-1] + x }
  dp = Array.new(n) { Array.new(n, 0) }
  (k..n).each do |length|
    (0..(n - length)).each do |i|
      j = i + length - 1
      best = Float::INFINITY
      i.step(j - 1, k - 1) do |m|
        best = [best, dp[i][m] + dp[m + 1][j]].min
      end
      dp[i][j] = best
      dp[i][j] += prefix[j + 1] - prefix[i] if (length - 1) % (k - 1) == 0
    end
  end
  dp[0][n - 1]
end
