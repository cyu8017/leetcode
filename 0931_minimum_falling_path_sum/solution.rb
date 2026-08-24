# LeetCode 0931 - Minimum Falling Path Sum
# https://leetcode.com/problems/minimum-falling-path-sum/

# @param {Integer[][]} matrix
# @return {Integer}
def min_falling_path_sum(matrix)
  dp = matrix[0].dup
  (1...matrix.length).each do |r|
    ndp = Array.new(dp.length, 0)
    dp.each_index do |c|
      best = dp[c]
      best = [best, dp[c - 1]].min if c > 0
      best = [best, dp[c + 1]].min if c + 1 < dp.length
      ndp[c] = matrix[r][c] + best
    end
    dp = ndp
  end
  dp.min
end
